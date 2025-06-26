import hashlib
from cryptography.fernet import Fernet

def compute_hash(data):
    return hashlib.sha256(data).hexdigest()

def load_key(key_path):
    with open(key_path, 'rb') as key_file:
        return key_file.read()
