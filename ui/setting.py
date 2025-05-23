from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt


class SettingsView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title = QLabel("Налаштування")
        title.setStyleSheet("font-size: 16pt; font-weight: bold; margin: 20px 0;")
        layout.addWidget(title)

        general_frame = QWidget()
        general_layout = QVBoxLayout(general_frame)
        general_layout.setContentsMargins(0,0,0,0)
        general_layout.setSpacing(10)

        general_label = QLabel("Загальні:")
        general_label.setStyleSheet("font-weight: bold;")
        general_layout.addWidget(general_label)

        self.auto_update = QCheckBox("Автооновлення")
        self.notifications = QCheckBox("Сповіщення")
        general_layout.addWidget(self.auto_update)
        general_layout.addWidget(self.notifications)

        layout.addWidget(general_frame)

        btn_frame = QWidget()
        btn_layout = QHBoxLayout(btn_frame)
        btn_layout.setContentsMargins(0,0,0,0)
        btn_layout.setSpacing(10)

        self.btn_save = QPushButton("Зберегти")
        self.btn_save.setFixedWidth(150)
        self.btn_default = QPushButton("За замовчуванням")
        self.btn_default.setFixedWidth(150)

        btn_layout.addWidget(self.btn_save)
        btn_layout.addWidget(self.btn_default)

        layout.addWidget(btn_frame)
