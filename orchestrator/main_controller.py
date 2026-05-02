

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mail.email_receiver import EmailReceiver
from mail.email_sender import EmailSender
from agent.agent import EmailAgent
from agent.intent_classifier import IntentClassifier
from negotiation.negotiation_engine import NegotiationEngine
from scheduler.scheduler import Scheduler
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
	memory = ConversationRepo()

	print("Fetching unread emails...")
	emails = receiver.fetch_unread_emails()
	for mail_obj in emails:
		thread_id = extract_thread_id(mail_obj)
		sender_addr = mail_obj['from']
		receiver_addr = sender.email_address
		content = mail_obj['body']
		print(f"\nProcessing email from {sender_addr} (thread: {thread_id})")
		# Store incoming message
		memory.add_message(thread_id, sender_addr, receiver_addr, content, direction="received")
		# Get conversation history (for context)
		history = memory.get_conversation(thread_id)
		# Detect intent
		intent = intent_classifier.classify_intent(content)
		print(f"Detected intent: {intent}")
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
		else:
			reply = agent.generate_reply(content, history=history)
		# Store reply
		memory.add_message(thread_id, receiver_addr, sender_addr, reply, direction="sent")
		# Send reply
		sender.send_email(sender_addr, f"Re: {thread_id}", reply)
		print(f"Replied to {sender_addr} for thread {thread_id}.")

if __name__ == "__main__":
	main()
