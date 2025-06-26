import os
import json
import base64
from datetime import datetime
from cryptography.fernet import Fernet
from utils import compute_hash, load_key


def encrypt_file(file_path, key_path, _unused_output_dir=None):
    key = load_key(key_path)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        file_data = file.read()

    file_hash = compute_hash(file_data)
    metadata = {
        'original_filename': os.path.basename(file_path),
        'timestamp': datetime.utcnow().isoformat(),
        'hash': file_hash
    }

    package = {
        'metadata': metadata,
        'file_data': base64.b64encode(file_data).decode('utf-8')
    }

    json_data = json.dumps(package).encode('utf-8')
    encrypted_data = fernet.encrypt(json_data)

    # Save encrypted file in the same directory as original
    out_filename = os.path.basename(file_path) + '.encrypted'
    out_path = os.path.join(os.path.dirname(file_path), out_filename)

    with open(out_path, 'wb') as enc_file:
        enc_file.write(encrypted_data)

    # ✅ Delete the original file after successful encryption
    os.remove(file_path)

    return out_path


def decrypt_file(file_path, key_path, _unused_output_dir=None):
    key = load_key(key_path)
    fernet = Fernet(key)

    with open(file_path, 'rb') as enc_file:
        encrypted_data = enc_file.read()

    decrypted_json = fernet.decrypt(encrypted_data)
    package = json.loads(decrypted_json)

    metadata = package['metadata']
    file_data = base64.b64decode(package['file_data'])

    if compute_hash(file_data) != metadata['hash']:
        raise ValueError("Tampering detected! File hash mismatch.")

    # Save the decrypted file in the same location as the encrypted file
    output_dir = os.path.dirname(file_path)
    out_path = os.path.join(output_dir, metadata['original_filename'])

    with open(out_path, 'wb') as dec_file:
        dec_file.write(file_data)

    # ✅ Delete the encrypted file after successful decryption
    os.remove(file_path)

    return out_path, metadata