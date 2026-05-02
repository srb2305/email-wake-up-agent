
# Google Calendar integration
import os
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'calendar_credentials.json'  # Path to your credentials file
CALENDAR_ID = 'primary'  # Or your specific calendar ID

class CalendarAdapter:
	def __init__(self):
		self.creds = service_account.Credentials.from_service_account_file(
			SERVICE_ACCOUNT_FILE, scopes=SCOPES)
		self.service = build('calendar', 'v3', credentials=self.creds)

	def create_event(self, summary, start_time, end_time, description=None):
		event = {
			'summary': summary,
			'description': description or '',
			'start': {
				'dateTime': start_time,
				'timeZone': 'UTC',
			},
			'end': {
				'dateTime': end_time,
				'timeZone': 'UTC',
			},
		}
		event = self.service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
		return event.get('htmlLink')
