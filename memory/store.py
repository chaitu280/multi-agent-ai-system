import sqlite3
import json
from datetime import datetime


DB_PATH = "data/agent_memory.db"


def initialize_memory():

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            created_at TEXT,
            user_query TEXT,
            final_answer TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS executions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            agent TEXT,
            status TEXT,
            timestamp TEXT,
            output TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_session(
    session_id,
    user_query,
    final_answer
):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO sessions
        VALUES (?, ?, ?, ?)
        """,
        (
            session_id,
            datetime.now().isoformat(),
            user_query,
            final_answer
        )
    )

    connection.commit()
    connection.close()


def save_execution(
    session_id,
    agent,
    status,
    output
):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO executions
        (
            session_id,
            agent,
            status,
            timestamp,
            output
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            session_id,
            agent,
            status,
            datetime.now().isoformat(),
            output
        )
    )

    connection.commit()
    connection.close()