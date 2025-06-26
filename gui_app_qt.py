import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLabel, QCheckBox, QMessageBox
)
from encryptor import generate_key, load_key, encrypt_file, decrypt_file

class SecureFileApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure File Storage - AES Encryption")
        self.setGeometry(100, 100, 400, 300)
        self.key_path = "secret.key"

        self.layout = QVBoxLayout()

        self.label = QLabel("Secure File Storage System")
        self.layout.addWidget(self.label)

        self.btn_generate = QPushButton("🔑 Generate Key")
        self.btn_generate.clicked.connect(self.generate_key)
        self.layout.addWidget(self.btn_generate)

        self.btn_encrypt = QPushButton("🔒 Encrypt File")
        self.btn_encrypt.clicked.connect(self.encrypt_file_gui)
        self.layout.addWidget(self.btn_encrypt)

        self.btn_decrypt = QPushButton("🔓 Decrypt File")
        self.btn_decrypt.clicked.connect(self.decrypt_file_gui)
        self.layout.addWidget(self.btn_decrypt)

        self.checkbox_delete = QCheckBox("Delete original file after encryption")
        self.layout.addWidget(self.checkbox_delete)

        self.status_label = QLabel("Status: Ready")
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

    def generate_key(self):
        generate_key(self.key_path)
        self.status_label.setText("✅ Key generated")

    def encrypt_file_gui(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Encrypt")
        if not file_path:
            return
        try:
            key = load_key(self.key_path)
            encrypt_file(file_path, key)
            if self.checkbox_delete.isChecked():
                os.remove(file_path)
            self.status_label.setText("✅ File encrypted successfully")
        except Exception as e:
            self.show_error("Encryption Error", str(e))

    def decrypt_file_gui(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Decrypt")
        if not file_path:
            return
        try:
            key = load_key(self.key_path)
            decrypt_file(file_path, key)
            self.status_label.setText("✅ File decrypted successfully")
        except Exception as e:
            self.show_error("Decryption Error", str(e))

    def show_error(self, title, message):
        self.status_label.setText(f"❌ {title}")
        QMessageBox.critical(self, title, message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SecureFileApp()
    window.show()
    sys.exit(app.exec_())
