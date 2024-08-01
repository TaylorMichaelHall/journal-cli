import re
import sqlite3
import uuid
from datetime import datetime
from pathlib import Path

DB_DIR = Path.home() / '.journal-cli'
DB_FILE = DB_DIR / 'journal.db'

def ensure_db_directory():
    DB_DIR.mkdir(parents=True, exist_ok=True)

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_table():
    ensure_db_directory()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries
                 (id TEXT PRIMARY KEY,
                  added_at TEXT,
                  updated_at TEXT,
                  entry TEXT)''')
    conn.commit()
    conn.close()

def get_current_time():
    return datetime.now().replace(microsecond=0).isoformat()

def sanitize_text(text):
    # Normalize newlines
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Trim trailing whitespace from each line
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    
    # Remove null bytes
    text = text.replace('\0', '')
    
    # Remove ANSI escape sequences
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    text = ansi_escape.sub('', text)
    
    # Limit overall length (e.g., to 10000 characters)
    max_length = 10000
    if len(text) > max_length:
        text = text[:max_length]
    
    return text

def add_entry_to_db(entry):
    sanitized_entry = sanitize_text(entry)
    current_time = get_current_time()
    entry_id = str(uuid.uuid4())
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO entries (id, added_at, updated_at, entry) VALUES (?, ?, ?, ?)",
              (entry_id, current_time, current_time, sanitized_entry))
    conn.commit()
    conn.close()
    return entry_id

def get_entries_from_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, added_at, updated_at, entry FROM entries ORDER BY added_at")
    entries = c.fetchall()
    conn.close()
    return entries

def edit_entry_in_db(id, new_entry):
    sanitized_entry = sanitize_text(new_entry)
    current_time = get_current_time()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE entries SET entry = ?, updated_at = ? WHERE id = ?",
              (sanitized_entry, current_time, id))
    rows_affected = c.rowcount
    conn.commit()
    conn.close()
    return rows_affected

def delete_entry_from_db(id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM entries WHERE id = ?", (id,))
    rows_affected = c.rowcount
    conn.commit()
    conn.close()
    return rows_affected