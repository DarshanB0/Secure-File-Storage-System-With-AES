from cryptography.fernet import Fernet

def generate_key(path='keys/key.key'):
    key = Fernet.generate_key()
    with open(path, 'wb') as f:
        f.write(key)
    print(f"[+] New key saved to {path}")
