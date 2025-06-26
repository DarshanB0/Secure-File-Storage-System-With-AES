import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from encryptor import encrypt_file, decrypt_file

class FileEncryptorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure File Encryptor")
        self.setGeometry(100, 100, 350, 150)

        layout = QVBoxLayout()

        encrypt_btn = QPushButton("Encrypt File")
        encrypt_btn.clicked.connect(self.encrypt_file_gui)
        layout.addWidget(encrypt_btn)

        decrypt_btn = QPushButton("Decrypt File")
        decrypt_btn.clicked.connect(self.decrypt_file)
        layout.addWidget(decrypt_btn)

        self.setLayout(layout)

    def encrypt_file_gui(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select file to encrypt")
        if path:
            try:
                output_path = encrypt_file(path, 'keys/key.key', 'encrypted_files')
                QMessageBox.information(self, "Success", f"✅ File encrypted!\nSaved to: {output_path}")
            except Exception as e:
                QMessageBox.critical(self, "Encryption Error", str(e))


    def decrypt_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select file to decrypt")
        if path:
            try:
                output_path, meta = decrypt_file(path, 'keys/key.key', 'decrypted_files')

                msg = (
                    f"File Decrypted Successfully!\n\n"
                    f"Original Filename: {meta['original_filename']}\n"
                    f"Encrypted At: {meta['timestamp']}\n"
                    f"SHA-256 Hash: {meta['hash']}\n"
                    f"Saved path: {output_path}"
                )
                QMessageBox.information(self, "Decryption Info", msg)

            except Exception as e:
                QMessageBox.critical(self, "Decryption Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileEncryptorApp()
    window.show()
    sys.exit(app.exec_())
