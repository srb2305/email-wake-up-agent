
from config.config_loader import Config

class NegotiationEngine:
	def __init__(self):
		self.config = Config()
		self.budget_limit = float(self.config.budget_limit or 0)

	def handle(self, email_text):
		# Simple logic: if user asks for more than budget, politely decline
		# Otherwise, agree to the proposed amount
		import re
		# Extract numbers from the email (very basic)
		numbers = re.findall(r'\d+', email_text.replace(',', ''))
		if numbers:
			requested = max(map(float, numbers))
			if requested > self.budget_limit:
				return f"Thank you for your interest. Unfortunately, our budget limit is {self.budget_limit:.2f} and we are unable to exceed it. Please let us know if you are still interested."
			else:
				return f"We can confirm the compensation of {requested:.2f} as it is within our budget. Looking forward to working with you!"
		return "Let's discuss the compensation further. Could you specify your expectations?"
