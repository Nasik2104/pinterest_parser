from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from core.key_manager import get_hwid, verify_key, save_license_key

class ActivationWidget(QWidget):
    def __init__(self, on_success_callback):
        super().__init__()
        self.on_success_callback = on_success_callback
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Активація")
        layout = QVBoxLayout()

        hwid = get_hwid()
        layout.addWidget(QLabel("Ваш HWID:"))
        layout.addWidget(QLabel(hwid))

        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Введіть ключ активації")
        layout.addWidget(self.key_input)

        btn = QPushButton("Активувати")
        btn.clicked.connect(self.check_key)
        layout.addWidget(btn)

        self.setLayout(layout)

    def check_key(self):
        hwid = get_hwid()
        key = self.key_input.text().strip()
        if verify_key(hwid, key):
            save_license_key(key)
            QMessageBox.information(self, "OK", "Активація успішна!")
            self.on_success_callback()
            self.close()
        else:
            QMessageBox.critical(self, "Помилка", "Невірний ключ!")
