import sqlite3
import hashlib
import os
import uuid

def get_hwid():
    return str(uuid.getnode())

def generate_key(hwid: str) -> str:
    return hashlib.sha256(hwid.encode()).hexdigest()[:16].upper()

def is_key_valid(db_path="license.db") -> bool:
    if not os.path.exists(db_path):
        return False
    hwid = get_hwid()
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS keys (key TEXT PRIMARY KEY)")
    cur.execute("SELECT 1 FROM keys WHERE key = ?", (generate_key(hwid),))
    return cur.fetchone() is not None
