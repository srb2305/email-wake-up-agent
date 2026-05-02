
import sqlite3
import os
from datetime import datetime

class ConversationRepo:
	def __init__(self, db_path='conversations.db'):
		self.db_path = db_path
		self._init_db()

	def _init_db(self):
		conn = sqlite3.connect(self.db_path)
		c = conn.cursor()
		c.execute('''
			CREATE TABLE IF NOT EXISTS conversations (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				thread_id TEXT,
				sender TEXT,
				receiver TEXT,
				content TEXT,
				timestamp TEXT,
				direction TEXT
			)
		''')
		conn.commit()
		conn.close()

	def add_message(self, thread_id, sender, receiver, content, direction):
		conn = sqlite3.connect(self.db_path)
		c = conn.cursor()
		c.execute('''
			INSERT INTO conversations (thread_id, sender, receiver, content, timestamp, direction)
			VALUES (?, ?, ?, ?, ?, ?)
		''', (thread_id, sender, receiver, content, datetime.utcnow().isoformat(), direction))
		conn.commit()
		conn.close()

	def get_conversation(self, thread_id):
		conn = sqlite3.connect(self.db_path)
		c = conn.cursor()
		c.execute('''
			SELECT sender, receiver, content, timestamp, direction FROM conversations
			WHERE thread_id = ? ORDER BY timestamp ASC
		''', (thread_id,))
		messages = c.fetchall()
		conn.close()
		return messages

	def get_all_threads(self):
		conn = sqlite3.connect(self.db_path)
		c = conn.cursor()
		c.execute('SELECT DISTINCT thread_id FROM conversations')
		threads = [row[0] for row in c.fetchall()]
		conn.close()
		return threads
