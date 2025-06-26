from PyQt5.QtWidgets import QApplication
from gui import CryptoApp
import sys
import os
from utils import generate_key

if __name__ == '__main__':
    os.makedirs('keys', exist_ok=True)
    os.makedirs('encrypted_files', exist_ok=True)
    os.makedirs('decrypted_files', exist_ok=True)

    if not os.path.exists('keys/key.key'):
        generate_key()

    app = QApplication(sys.argv)
    win = CryptoApp()
    win.show()
    sys.exit(app.exec_())
