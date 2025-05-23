from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QCheckBox, QPushButton
from PyQt6.QtCore import Qt

class ParserView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title = QLabel("Збір даних")
        title.setStyleSheet("font-size: 16pt; font-weight: bold; margin: 20px 0;")
        layout.addWidget(title)

        query_frame = QWidget()
        query_layout = QHBoxLayout(query_frame)
        query_layout.setContentsMargins(0,0,0,0)
        query_layout.setSpacing(5)

        query_label = QLabel("Пошукові запити:")
        self.query_entry = QLineEdit()
        self.query_entry.setFixedWidth(300)
        query_layout.addWidget(query_label)
        query_layout.addWidget(self.query_entry)

        layout.addWidget(query_frame)

        options_frame = QWidget()
        options_layout = QHBoxLayout(options_frame)
        options_layout.setContentsMargins(0,0,0,0)
        options_layout.setSpacing(10)

        self.deep_scan = QCheckBox("Глибокий парсинг")
        self.save_images = QCheckBox("Зберігати зображення")
        options_layout.addWidget(self.deep_scan)
        options_layout.addWidget(self.save_images)

        layout.addWidget(options_frame)

        btn_frame = QWidget()
        btn_layout = QHBoxLayout(btn_frame)
        btn_layout.setContentsMargins(0,0,0,0)
        btn_layout.setSpacing(10)

        self.btn_start = QPushButton("Почати парсинг")
        self.btn_start.setFixedWidth(150)
        self.btn_cancel = QPushButton("Скасувати")
        self.btn_cancel.setFixedWidth(150)

        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_cancel)

        layout.addWidget(btn_frame)
