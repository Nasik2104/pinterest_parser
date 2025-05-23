from PyQt6.QtWidgets import QApplication
import sys
from core.key_manager import get_hwid, verify_key, init_db, load_license_key
from ui.activation_widget import ActivationWidget
from ui.ui_mainwindow import MainWindow

def is_activated():
    key = load_license_key()
    return key and verify_key(get_hwid(), key)

def main():
    init_db()
    app = QApplication(sys.argv)

    def launch_main():
        window = MainWindow()
        window.show()

    if is_activated():
        launch_main()
    else:
        activation = ActivationWidget(on_success_callback=launch_main)
        activation.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
