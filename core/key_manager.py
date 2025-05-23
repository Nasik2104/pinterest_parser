import hashlib
import uuid

def get_hwid():
    return str(uuid.getnode())

def verify_key(hwid, key):
    hashed = hashlib.sha256(hwid.encode()).hexdigest()[:16].upper()
    return key == hashed

def generate_key(hwid):
    return hashlib.sha256(hwid.encode()).hexdigest()[:16].upper()
