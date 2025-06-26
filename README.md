# Secure File Storage System with AES Encryption

The Secure File Storage System is designed to help users encrypt sensitive files using symmetric AES encryption. It ensures that no readable copy of the file remains after encryption and verifies the integrity of the file during decryption using a cryptographic hash.

## Features

  - AES Encryption/Decryption using Fernet (symmetric encryption)
  - Metadata storage: original filename, timestamp, hash
  - Tamper detection via SHA-256 hash verification
  - Deletes original file after encryption
  - Deletes encrypted file after decryption
  - Saves encrypted/decrypted files in the same location as original

## Technologies Used

  - Python 3.13.3
  - cryptography (Fernet)
  - PyQt5

## Installation & Setup

  1. Clone this repository or download the files.
  2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```
  3. Install dependencies:
   ```
   pip install pyqt5 cryptography
   ```
  4. Generate the key using `key_manager.py`:
   ```
   python -c "from key_manager import generate_key; generate_key()"
   ```
  5. Run the GUI:
   ```
   python gui.py
   ```

## Folder Structure

  - encryptor.py – handles both encryption and decryption logic with tamper detection
  - gui.py – PyQt5 GUI interface
  - key_manager.py – key generation and loading
  - utils.py – utility functions for hashing and key loading
  - keys/key.key – auto-generated key file
  - README.md – project info

## How It Works

### Encryption Process
  1. User selects a file.
  2. The program reads the file and computes a SHA-256 hash.
  3. Metadata is created: original filename, hash, and timestamp.
  4. The file data and metadata are packed into a JSON object and encrypted using Fernet.
  5. The encrypted file is saved as `<originalname>.encrypted` in the same folder.
  6. The original file is deleted for security.

### Decryption Process
  1. User selects the `.encrypted` file.
  2. It is decrypted using the stored key.
  3. The JSON package is unpacked and verified using the stored hash.
  4. If the hash matches, the file is restored to its original location.
  5. The encrypted file is deleted.

## Security Features
  - AES encryption via Fernet (uses AES-128 + HMAC + IV + padding).
  - SHA-256 hash ensures the file wasn't modified (tamper detection).
  - Secret key is stored in a separate file and not embedded in the script.

