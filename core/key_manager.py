import sqlite3, os, hashlib
from uuid import getnode

def get_hwid():
    return str(getnode())

def verify_key(hwid, key):
    expected = hashlib.sha256(hwid.encode()).hexdigest()[:16].upper()
    return key == expected

def init_db():
    conn = sqlite3.connect("license.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS license (
            key TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_license_key(key):
    conn = sqlite3.connect("license.db")
    c = conn.cursor()
    c.execute("DELETE FROM license")
    c.execute("INSERT INTO license (key) VALUES (?)", (key,))
    conn.commit()
    conn.close()

def load_license_key():
    if not os.path.exists("license.db"):
        return None
    conn = sqlite3.connect("license.db")
    c = conn.cursor()
    c.execute("SELECT key FROM license")
    row = c.fetchone()
    conn.close()
    return row[0] if row else None
