from PyQt6.QtWidgets import QApplication
import sys, json, os
from core.key_manager import get_hwid, verify_key
from ui.activation_widget import ActivationWidget
from ui.ui_mainwindow import MainWindow

def is_activated():
    if not os.path.exists("license.json"):
        return False
    with open("license.json", "r") as f:
        data = json.load(f)
    return verify_key(get_hwid(), data.get("key", ""))

def main():
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
