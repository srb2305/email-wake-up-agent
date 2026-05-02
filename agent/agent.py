
import openai
from config.config_loader import Config


class EmailAgent:
	def __init__(self):
		self.config = Config()
		openai.api_key = self.config.openai_api_key

	def generate_reply(self, prompt, history=None):
		messages = [{"role": "system", "content": self.config.gig_description or "You are an email agent."}]
		# Add conversation history if provided
		if history:
			for sender, receiver, content, timestamp, direction in history:
				role = "user" if direction == "received" else "assistant"
				messages.append({"role": role, "content": content})
		# Add the latest prompt as the last user message
		messages.append({"role": "user", "content": prompt})
		response = openai.chat.completions.create(
			model="gpt-3.5-turbo",
			messages=messages
		)
		return response.choices[0].message.content
