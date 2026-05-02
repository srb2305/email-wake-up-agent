import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mail.email_receiver import EmailReceiver
from mail.email_sender import EmailSender
from agent.agent import EmailAgent
from agent.intent_classifier import IntentClassifier
from negotiation.negotiation_engine import NegotiationEngine
from scheduler.scheduler import Scheduler
from scheduler.calendar_adapter import CalendarAdapter
from memory.conversation_repo import ConversationRepo

def extract_thread_id(email_obj):
	# Use subject as thread_id for simplicity; in production, use Message-ID or thread headers
	return email_obj['subject']

def main():
	receiver = EmailReceiver()
	sender = EmailSender()
	agent = EmailAgent()
	intent_classifier = IntentClassifier()
	negotiation_engine = NegotiationEngine()

	scheduler = Scheduler()
	calendar = CalendarAdapter()
	memory = ConversationRepo()

	logging.info("Fetching unread emails...")
	try:
		emails = receiver.fetch_unread_emails()
	except Exception as e:
		logging.error(f"Failed to fetch emails: {e}")
		return
	for mail_obj in emails:
		try:
			thread_id = extract_thread_id(mail_obj)
			sender_addr = mail_obj['from']
			receiver_addr = sender.email_address
			content = mail_obj['body']
			logging.info(f"Processing email from {sender_addr} (thread: {thread_id})")
			# Store incoming message
			memory.add_message(thread_id, sender_addr, receiver_addr, content, direction="received")
			# Get conversation history (for context)
			history = memory.get_conversation(thread_id)
			# Detect intent
			intent = intent_classifier.classify_intent(content)
			logging.info(f"Detected intent: {intent}")
			# Handle negotiation, scheduling, or default to agent
			if intent == "NEGOTIATION":
				reply = negotiation_engine.handle(content)
			elif intent in ("SCHEDULE", "RESCHEDULE"):
				slots = scheduler.propose_slots()
				reply = (
					"Here are some available time slots for a call:\n" +
					"\n".join(f"- {slot}" for slot in slots) +
					"\nPlease reply with your preferred slot."
				)
			elif any(slot in content for slot in scheduler.propose_slots()):
				# User replied with a slot confirmation
				confirmed_slot = next((slot for slot in scheduler.propose_slots() if slot in content), None)
				if confirmed_slot:
					from datetime import datetime, timedelta
					start_dt = datetime.strptime(confirmed_slot, '%Y-%m-%d %H:%M')
					end_dt = start_dt + timedelta(minutes=30)
					try:
						event_link = calendar.create_event(
							summary="Call with Prospect",
							start_time=start_dt.isoformat(),
							end_time=end_dt.isoformat(),
							description="Scheduled via Email Wake-Up Agent"
						)
						reply = f"Your meeting is confirmed for {confirmed_slot}. Here is your Google Calendar link: {event_link}"
						logging.info(f"Created calendar event for {sender_addr} at {confirmed_slot}")
					except Exception as ce:
						reply = "There was an error scheduling your meeting. Please try again later."
						logging.error(f"Calendar event creation failed: {ce}")
				else:
					reply = "Sorry, I could not recognize the slot you selected. Please reply with one of the proposed slots."
			else:
				reply = agent.generate_reply(content, history=history)
			# Store reply
			memory.add_message(thread_id, receiver_addr, sender_addr, reply, direction="sent")
			# Send reply
			sender.send_email(sender_addr, f"Re: {thread_id}", reply)
			logging.info(f"Replied to {sender_addr} for thread {thread_id}.")
		except Exception as e:
			logging.error(f"Error processing email from {mail_obj.get('from')}: {e}")

if __name__ == "__main__":
	main()
