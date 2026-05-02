
import openai
from config.config_loader import Config

class IntentClassifier:
	def __init__(self):
		self.config = Config()
		openai.api_key = self.config.openai_api_key

	def classify_intent(self, email_text):
		prompt = (
			"Classify the intent of the following email as one of: "
			"INTERESTED, CURIOUS, NEGOTIATION, DECLINING, NO_RESPONSE, SCHEDULE, RESCHEDULE.\n"
			f"Email: {email_text}\nIntent:"
		)
		response = openai.chat.completions.create(
			model="gpt-3.5-turbo",
			messages=[{"role": "user", "content": prompt}]
		)
		intent = response.choices[0].message.content.strip().split()[0].upper()
		return intent
