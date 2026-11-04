from ui.ui_main import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QPixmap
import os

import ui.resources_rc

class MainWindow(QMainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/resources/taiga_flag.png"))
        self.ui.selectFileButton.clicked.connect(self.request_file_for_display_picture)
        self.ui.reloadPreviewImage.clicked.connect(lambda: self.ui.displayPictureDisplay.setPixmap(QPixmap(self.ui.fileSelectedIndicator.text())))

        #Setup actions
        self.ui.actionClose.triggered.connect(self.app.quit)

    @Slot()
    def request_file_for_display_picture(self) -> None:
        self.file = QFileDialog.getOpenFileName(self, "Select a 30x40 image or multiples", os.path.expanduser("~"), "Images (*.png *.jpeg)")
        self.ui.fileSelectedIndicator.setText(self.file[0])
        self.ui.displayPictureDisplay.setPixmap(QPixmap(self.ui.fileSelectedIndicator.text()))