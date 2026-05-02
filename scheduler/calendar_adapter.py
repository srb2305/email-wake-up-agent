
# Google Calendar integration
import os
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config.config_loader import Config

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'calendar_credentials.json'  # Path to your credentials file

class CalendarAdapter:
	def __init__(self):
		self.config = Config()
		self.creds = service_account.Credentials.from_service_account_file(
			SERVICE_ACCOUNT_FILE, scopes=SCOPES)
		self.service = build('calendar', 'v3', credentials=self.creds)
		self.calendar_id = self.config.calendar_id
		self.timezone = self.config.calendar_timezone

	def create_event(self, summary, start_time, end_time, description=None):
		event = {
			'summary': summary,
			'description': description or '',
			'start': {
				'dateTime': start_time,
				'timeZone': self.timezone,
			},
			'end': {
				'dateTime': end_time,
				'timeZone': self.timezone,
			},
		}
		event = self.service.events().insert(calendarId=self.calendar_id, body=event).execute()
		return event.get('htmlLink')
