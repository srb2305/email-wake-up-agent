
from datetime import datetime, timedelta

class Scheduler:
	def __init__(self):
		# In a real system, integrate with Google Calendar or similar
		self.available_slots = self._generate_slots()

	def _generate_slots(self):
		# Generate next 3 available slots (mock)
		now = datetime.now()
		return [
			(now + timedelta(days=1, hours=10)).strftime('%Y-%m-%d %H:%M'),
			(now + timedelta(days=2, hours=15)).strftime('%Y-%m-%d %H:%M'),
			(now + timedelta(days=3, hours=11)).strftime('%Y-%m-%d %H:%M'),
		]

	def propose_slots(self):
		return self.available_slots

	def confirm_slot(self, slot):
		if slot in self.available_slots:
			self.available_slots.remove(slot)
			return True
		return False
