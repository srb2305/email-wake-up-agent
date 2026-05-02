
import os
from dotenv import load_dotenv

class Config:
	def __init__(self, env_path='.env'):
		load_dotenv(env_path)
		self.openai_api_key = os.getenv('OPENAI_API_KEY')
		self.gig_description = os.getenv('GIG_DESCRIPTION')
		self.budget_limit = os.getenv('BUDGET_LIMIT')
		self.tone = os.getenv('TONE')
		self.email_address = os.getenv('EMAIL_ADDRESS')
		self.email_password = os.getenv('EMAIL_PASSWORD')

	def as_dict(self):
		return {
			'openai_api_key': self.openai_api_key,
			'gig_description': self.gig_description,
			'budget_limit': self.budget_limit,
			'tone': self.tone,
			'email_address': self.email_address,
			'email_password': self.email_password
		}
