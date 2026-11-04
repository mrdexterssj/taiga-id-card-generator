# This is the app's entrypoint
# It sets up env vars and loads config, then launches the GUI

from PySide6.QtWidgets import QApplication
from setup_ui import MainWindow
import sys

#Launch GUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()

    sys.exit(app.exec())