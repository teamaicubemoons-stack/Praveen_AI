import sqlite3
import json
import os
from datetime import datetime

class MemoryService:
    def __init__(self, db_path="chat_history.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initializes the database if it doesn't exist."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                sender_id TEXT,
                role TEXT,
                content TEXT,
                timestamp DATETIME
            )
        ''')
        conn.commit()
        conn.close()

    def add_message(self, sender_id: str, role: str, content: str):
        """Adds a message to the history."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO history (sender_id, role, content, timestamp) VALUES (?, ?, ?, ?)",
            (sender_id, role, content, datetime.now())
        )
        conn.commit()
        conn.close()

    def get_history(self, sender_id: str, limit: int = 10):
        """Retrieves the last N messages for a user in OpenAI format."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT role, content FROM history WHERE sender_id = ? ORDER BY timestamp DESC LIMIT ?",
            (sender_id, limit)
        )
        rows = cursor.fetchall()
        conn.close()
        
        # Reverse to get chronological order
        history = [{"role": row[0], "content": row[1]} for row in reversed(rows)]
        return history

memory_service = MemoryService()
