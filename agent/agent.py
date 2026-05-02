
import openai
from config.config_loader import Config

class EmailAgent:
	def __init__(self):
		self.config = Config()
		openai.api_key = self.config.openai_api_key

	def generate_reply(self, prompt):
		response = openai.chat.completions.create(
			model="gpt-3.5-turbo",
			messages=[
				{"role": "system", "content": self.config.gig_description or "You are an email agent."},
				{"role": "user", "content": prompt}
			]
		)
		return response.choices[0].message.content
