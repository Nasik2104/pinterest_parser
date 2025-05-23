from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QCheckBox, QPushButton
from PyQt6.QtCore import Qt


class FilterView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title = QLabel("Фільтрація даних")
        title.setStyleSheet("font-size: 16pt; font-weight: bold; margin: 20px 0;")
        layout.addWidget(title)

        crit_frame = QWidget()
        crit_layout = QHBoxLayout(crit_frame)
        crit_layout.setContentsMargins(0,0,0,0)
        crit_layout.setSpacing(10)

        crit_label = QLabel("Критерії фільтрації:")
        crit_label.setStyleSheet("margin-right: 10px;")
        crit_layout.addWidget(crit_label)

        self.filter_min = QLineEdit()
        self.filter_min.setFixedWidth(100)
        self.filter_min.setPlaceholderText("Мін. значення")
        self.filter_max = QLineEdit()
        self.filter_max.setFixedWidth(100)
        self.filter_max.setPlaceholderText("Макс. значення")

        crit_layout.addWidget(self.filter_min)
        crit_layout.addWidget(self.filter_max)

        layout.addWidget(crit_frame)

        self.remove_duplicates = QCheckBox("Видалити дублікати")
        layout.addWidget(self.remove_duplicates)

        btn_frame = QWidget()
        btn_layout = QHBoxLayout(btn_frame)
        btn_layout.setContentsMargins(0,0,0,0)
        btn_layout.setSpacing(10)

        self.btn_apply = QPushButton("Застосувати фільтри")
        self.btn_apply.setFixedWidth(150)
        self.btn_reset = QPushButton("Скинути")
        self.btn_reset.setFixedWidth(150)

        btn_layout.addWidget(self.btn_apply)
        btn_layout.addWidget(self.btn_reset)

        layout.addWidget(btn_frame)
