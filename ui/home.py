from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
from PyQt6.QtCore import Qt

class HomeView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.welcome_label = QLabel("Ласкаво просимо до PinMetrical X")
        self.welcome_label.setStyleSheet("font-size: 18pt; font-weight: bold; margin: 50px 0;")
        layout.addWidget(self.welcome_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        stats_frame = QWidget()
        stats_layout = QGridLayout(stats_frame)
        stats_layout.setContentsMargins(20, 0, 20, 0)
        stats_layout.setSpacing(10)

        self.last_parse = QLabel("Останній парсинг: Немає даних")
        self.last_filter = QLabel("Остання фільтрація: Немає даних")

        stats_layout.addWidget(self.last_parse, 0, 0)
        stats_layout.addWidget(self.last_filter, 1, 0)

        layout.addWidget(stats_frame)
