from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget, QComboBox
)
from PyQt6.QtCore import Qt, QEasingCurve, QPropertyAnimation
from ui.home import HomeView
from core.parser_handler import ParserView
from ui.filter import FilterView
from ui.setting import SettingsView


class SidebarButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setCheckable(True)
        self.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                border: none;
                text-align: left;
                font-weight: bold;
                color: white;
                background-color: #2f3136;
                border-radius: 6px;
            }
            QPushButton:checked {
                background-color: #5865f2;
                color: white;
            }
            QPushButton:hover {
                background-color: #40444b;
            }
        """)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PinMetrical X")
        self.resize(900, 650)
        self.setMinimumSize(800, 600)
        self.setStyleSheet("background-color: #202225; color: white;")

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.sidebar = QWidget()
        self.sidebar.setFixedWidth(220)
        self.sidebar.setStyleSheet("background-color: #2f3136;")
        side_layout = QVBoxLayout(self.sidebar)
        side_layout.setContentsMargins(20, 20, 20, 20)
        side_layout.setSpacing(15)

        self.logo = QLabel("PinMetrical X")
        self.logo.setStyleSheet("font-size: 24pt; font-weight: bold; color: white; margin-bottom: 20px;")
        side_layout.addWidget(self.logo)

        self.btn_home = SidebarButton("Головна")
        self.btn_parse = SidebarButton("Збір даних")
        self.btn_filter = SidebarButton("Фільтрація")
        self.btn_settings = SidebarButton("Налаштування")

        side_layout.addWidget(self.btn_home)
        side_layout.addWidget(self.btn_parse)
        side_layout.addWidget(self.btn_filter)
        side_layout.addWidget(self.btn_settings)
        side_layout.addStretch()

        self.theme_label = QLabel("Тема:")
        self.theme_label.setStyleSheet("margin-top: 20px; font-weight: bold;")
        side_layout.addWidget(self.theme_label)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Світла", "Темна", "Система"])
        self.theme_combo.setStyleSheet("""
            QComboBox {
                padding: 5px 10px;
                border-radius: 6px;
                background-color: #40444b;
                color: white;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        side_layout.addWidget(self.theme_combo)

        main_layout.addWidget(self.sidebar)

        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack, 1)

        self.home_view = HomeView()
        self.parser_view = ParserView()
        self.filter_view = FilterView()
        self.settings_view = SettingsView()

        self.stack.addWidget(self.home_view)
        self.stack.addWidget(self.parser_view)
        self.stack.addWidget(self.filter_view)
        self.stack.addWidget(self.settings_view)

        self.status_bar = QLabel("Готово до роботи")
        self.status_bar.setFixedHeight(28)
        self.status_bar.setStyleSheet("background-color: #2f3136; padding-left: 15px; color: white; font-weight: bold;")

        layout_wrap = QVBoxLayout()
        layout_wrap.setContentsMargins(0, 0, 0, 0)
        layout_wrap.setSpacing(0)
        layout_wrap.addLayout(main_layout)
        layout_wrap.addWidget(self.status_bar)
        self.setLayout(layout_wrap)

        self.btn_home.clicked.connect(lambda: self.set_page(0))
        self.btn_parse.clicked.connect(lambda: self.set_page(1))
        self.btn_filter.clicked.connect(lambda: self.set_page(2))
        self.btn_settings.clicked.connect(lambda: self.set_page(3))

        self.theme_combo.currentTextChanged.connect(self.change_theme)

        self.btn_home.setChecked(True)

        self.anim = QPropertyAnimation(self.stack, b"geometry")
        self.anim.setDuration(300)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutCubic)

    def set_page(self, index):
        for btn in (self.btn_home, self.btn_parse, self.btn_filter, self.btn_settings):
            btn.setChecked(False)

        btns = [self.btn_home, self.btn_parse, self.btn_filter, self.btn_settings]
        btns[index].setChecked(True)

        start_geom = self.stack.geometry()
        self.anim.stop()
        self.anim.setStartValue(start_geom)
        self.stack.setCurrentIndex(index)
        self.anim.setEndValue(start_geom)
        self.anim.start()

        titles = ["Головна", "Збір даних", "Фільтрація", "Налаштування"]
        self.status_bar.setText(f"Ви на сторінці: {titles[index]}")

    def change_theme(self, t):
        if t == "Світла":
            self.setStyleSheet("background-color: white; color: black;")
            self.sidebar.setStyleSheet("background-color: #dfe3e6;")
            self.status_bar.setStyleSheet("background-color: #ccc; color: black; padding-left: 15px; font-weight: bold;")
        elif t == "Темна":
            self.setStyleSheet("background-color: #202225; color: white;")
            self.sidebar.setStyleSheet("background-color: #2f3136;")
            self.status_bar.setStyleSheet("background-color: #2f3136; padding-left: 15px; color: white; font-weight: bold;")
        else:
            self.setStyleSheet("")
            self.sidebar.setStyleSheet("")
            self.status_bar.setStyleSheet("")

