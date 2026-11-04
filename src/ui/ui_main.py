# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainpFnQuk.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QToolBar, QWidget)
import ui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(911, 600)
        MainWindow.setStyleSheet(u"")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon = QIcon(QIcon.fromTheme(u"window-close"))
        self.actionClose.setIcon(icon)
        self.actionGenerateNewIDCard = QAction(MainWindow)
        self.actionGenerateNewIDCard.setObjectName(u"actionGenerateNewIDCard")
        icon1 = QIcon(QIcon.fromTheme(u"entry-new"))
        self.actionGenerateNewIDCard.setIcon(icon1)
        self.actionVerifyIDAuthenticity = QAction(MainWindow)
        self.actionVerifyIDAuthenticity.setObjectName(u"actionVerifyIDAuthenticity")
        icon2 = QIcon(QIcon.fromTheme(u"view-certificate"))
        self.actionVerifyIDAuthenticity.setIcon(icon2)
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        icon3 = QIcon(QIcon.fromTheme(u"help-about"))
        self.actionAboutQt.setIcon(icon3)
        self.actionAboutQt.setMenuRole(QAction.MenuRole.AboutQtRole)
        self.actionAboutThisApp = QAction(MainWindow)
        self.actionAboutThisApp.setObjectName(u"actionAboutThisApp")
        self.actionAboutThisApp.setIcon(icon3)
        self.actionSeeTheProjectSGitHubPage = QAction(MainWindow)
        self.actionSeeTheProjectSGitHubPage.setObjectName(u"actionSeeTheProjectSGitHubPage")
        icon4 = QIcon(QIcon.fromTheme(u"open-link"))
        self.actionSeeTheProjectSGitHubPage.setIcon(icon4)
        self.actionLearnMoreAboutTheNewTaigaRepublic = QAction(MainWindow)
        self.actionLearnMoreAboutTheNewTaigaRepublic.setObjectName(u"actionLearnMoreAboutTheNewTaigaRepublic")
        self.actionLearnMoreAboutTheNewTaigaRepublic.setIcon(icon4)
        self.actionPreviewID = QAction(MainWindow)
        self.actionPreviewID.setObjectName(u"actionPreviewID")
        icon5 = QIcon(QIcon.fromTheme(u"preview"))
        self.actionPreviewID.setIcon(icon5)
        self.actionPreviewID.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 12, 0, 1, 1)

        self.maleRadioButton = QRadioButton(self.centralwidget)
        self.maleRadioButton.setObjectName(u"maleRadioButton")

        self.gridLayout.addWidget(self.maleRadioButton, 10, 2, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.fileSelectedIndicator = QLineEdit(self.centralwidget)
        self.fileSelectedIndicator.setObjectName(u"fileSelectedIndicator")
        self.fileSelectedIndicator.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.fileSelectedIndicator, 4, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 8, 10, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)

        self.aliasOptional = QLineEdit(self.centralwidget)
        self.aliasOptional.setObjectName(u"aliasOptional")

        self.gridLayout.addWidget(self.aliasOptional, 9, 2, 1, 8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 3, 5, 8)

        self.residencyCombobox = QComboBox(self.centralwidget)
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.addItem("")
        self.residencyCombobox.setObjectName(u"residencyCombobox")

        self.gridLayout.addWidget(self.residencyCombobox, 12, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)

        self.femaleRadioButton = QRadioButton(self.centralwidget)
        self.femaleRadioButton.setObjectName(u"femaleRadioButton")

        self.gridLayout.addWidget(self.femaleRadioButton, 10, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 9, 10, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 11, 3, 1, 8)

        self.displayPictureDisplay = QLabel(self.centralwidget)
        self.displayPictureDisplay.setObjectName(u"displayPictureDisplay")
        self.displayPictureDisplay.setMinimumSize(QSize(120, 120))
        self.displayPictureDisplay.setMaximumSize(QSize(120, 120))
        self.displayPictureDisplay.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #c0c0bd;\n"
"margin-left: 30px")
        self.displayPictureDisplay.setFrameShape(QFrame.Shape.NoFrame)
        self.displayPictureDisplay.setFrameShadow(QFrame.Shadow.Raised)
        self.displayPictureDisplay.setScaledContents(True)
        self.displayPictureDisplay.setWordWrap(True)

        self.gridLayout.addWidget(self.displayPictureDisplay, 3, 2, 4, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 15, 0, 1, 10)

        self.occupationCombobox = QComboBox(self.centralwidget)
        self.occupationCombobox.addItem("")
        self.occupationCombobox.addItem("")
        self.occupationCombobox.addItem("")
        self.occupationCombobox.addItem("")
        self.occupationCombobox.setObjectName(u"occupationCombobox")

        self.gridLayout.addWidget(self.occupationCombobox, 11, 2, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 13, 0, 1, 11)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 2, 1, 9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 5, 1, 6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 12, 3, 1, 8)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 11, 0, 1, 1)

        self.genderOther = QLineEdit(self.centralwidget)
        self.genderOther.setObjectName(u"genderOther")

        self.gridLayout.addWidget(self.genderOther, 10, 8, 1, 1)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 14, 0, 1, 11)

        self.idNumber = QLineEdit(self.centralwidget)
        self.idNumber.setObjectName(u"idNumber")

        self.gridLayout.addWidget(self.idNumber, 0, 2, 1, 3)

        self.otherGenderRadioButton = QRadioButton(self.centralwidget)
        self.otherGenderRadioButton.setObjectName(u"otherGenderRadioButton")

        self.gridLayout.addWidget(self.otherGenderRadioButton, 10, 4, 1, 4)

        self.displayName = QLineEdit(self.centralwidget)
        self.displayName.setObjectName(u"displayName")

        self.gridLayout.addWidget(self.displayName, 8, 2, 1, 8)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        icon6 = QIcon(QIcon.fromTheme(u"checkbox"))
        self.generateButton.setIcon(icon6)

        self.gridLayout.addWidget(self.generateButton, 15, 10, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 7, 2, 1, 9)

        self.reloadPreviewImage = QPushButton(self.centralwidget)
        self.reloadPreviewImage.setObjectName(u"reloadPreviewImage")
        icon7 = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.reloadPreviewImage.setIcon(icon7)

        self.gridLayout.addWidget(self.reloadPreviewImage, 4, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 2)

        self.selectFileButton = QPushButton(self.centralwidget)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setMinimumSize(QSize(140, 0))
        self.selectFileButton.setMaximumSize(QSize(1400, 16777215))
        icon8 = QIcon(QIcon.fromTheme(u"document-open"))
        self.selectFileButton.setIcon(icon8)

        self.gridLayout.addWidget(self.selectFileButton, 3, 0, 1, 2)

        self.preferNotSayRadioButton = QRadioButton(self.centralwidget)
        self.preferNotSayRadioButton.setObjectName(u"preferNotSayRadioButton")

        self.gridLayout.addWidget(self.preferNotSayRadioButton, 10, 9, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 911, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuID = QMenu(self.menubar)
        self.menuID.setObjectName(u"menuID")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAboutTaigaIDGenerator = QMenu(self.menuAbout)
        self.menuAboutTaigaIDGenerator.setObjectName(u"menuAboutTaigaIDGenerator")
        self.menuAboutTaigaIDGenerator.setIcon(icon3)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuID.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionPreviewID)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuID.addAction(self.actionGenerateNewIDCard)
        self.menuID.addAction(self.actionVerifyIDAuthenticity)
        self.menuAbout.addAction(self.menuAboutTaigaIDGenerator.menuAction())
        self.menuAbout.addAction(self.actionAboutQt)
        self.menuAboutTaigaIDGenerator.addAction(self.actionAboutThisApp)
        self.menuAboutTaigaIDGenerator.addAction(self.actionSeeTheProjectSGitHubPage)
        self.menuAboutTaigaIDGenerator.addAction(self.actionLearnMoreAboutTheNewTaigaRepublic)
        self.toolBar.addAction(self.actionGenerateNewIDCard)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionVerifyIDAuthenticity)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreviewID)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Taiga ID Generator", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
#if QT_CONFIG(statustip)
        self.actionClose.setStatusTip(QCoreApplication.translate("MainWindow", u"Closes the application", None))
#endif // QT_CONFIG(statustip)
        self.actionGenerateNewIDCard.setText(QCoreApplication.translate("MainWindow", u"Generate new ID Card", None))
#if QT_CONFIG(statustip)
        self.actionGenerateNewIDCard.setStatusTip(QCoreApplication.translate("MainWindow", u"Clears all fields and allow the creation of a new ID Card", None))
#endif // QT_CONFIG(statustip)
        self.actionVerifyIDAuthenticity.setText(QCoreApplication.translate("MainWindow", u"Verify ID Authenticity", None))
#if QT_CONFIG(statustip)
        self.actionVerifyIDAuthenticity.setStatusTip(QCoreApplication.translate("MainWindow", u"Verifies if an ID Card is authentic and hasn't been tampered with", None))
#endif // QT_CONFIG(statustip)
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
#if QT_CONFIG(statustip)
        self.actionAboutQt.setStatusTip(QCoreApplication.translate("MainWindow", u"Learn more about Qt", None))
#endif // QT_CONFIG(statustip)
        self.actionAboutThisApp.setText(QCoreApplication.translate("MainWindow", u"About this app", None))
#if QT_CONFIG(statustip)
        self.actionAboutThisApp.setStatusTip(QCoreApplication.translate("MainWindow", u"Shows more information about this app", None))
#endif // QT_CONFIG(statustip)
        self.actionSeeTheProjectSGitHubPage.setText(QCoreApplication.translate("MainWindow", u"See the project's GitHub page", None))
#if QT_CONFIG(statustip)
        self.actionSeeTheProjectSGitHubPage.setStatusTip(QCoreApplication.translate("MainWindow", u"Opens the project's GitHub page in your default browser", None))
#endif // QT_CONFIG(statustip)
        self.actionLearnMoreAboutTheNewTaigaRepublic.setText(QCoreApplication.translate("MainWindow", u"Learn more about The New Taiga Republic", None))
#if QT_CONFIG(statustip)
        self.actionLearnMoreAboutTheNewTaigaRepublic.setStatusTip(QCoreApplication.translate("MainWindow", u"Opens the INSMP's Wiki entry on The New Taiga Republic on your default browser", None))
#endif // QT_CONFIG(statustip)
        self.actionPreviewID.setText(QCoreApplication.translate("MainWindow", u"Preview ID", None))
#if QT_CONFIG(statustip)
        self.actionPreviewID.setStatusTip(QCoreApplication.translate("MainWindow", u"Shows a preview of the ID Card before exporting", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MainWindow", u"Your Minecraft username", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Display name:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Place of residency:", None))
        self.maleRadioButton.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#c0c0bd;\">ID Number:</span></p></body></html>", None))
        self.fileSelectedIndicator.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No file selected", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("MainWindow", u"It can be anything that identifies you (e.g.: your Discord username)", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Alias (optional):", None))
        self.residencyCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"\U0001f417 I don't have a city (No city)", None))
        self.residencyCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"\U0001f339 Scarlet City", None))
        self.residencyCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"\U0001f353 Sweet Berry City", None))
        self.residencyCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"\U0001f341 Toronto", None))
        self.residencyCombobox.setItemText(4, QCoreApplication.translate("MainWindow", u"\U0001f331 Podzol Port", None))
        self.residencyCombobox.setItemText(5, QCoreApplication.translate("MainWindow", u"\U0001f3b0 Las Vegas", None))
        self.residencyCombobox.setItemText(6, QCoreApplication.translate("MainWindow", u"\U0001f98a Fox Town", None))
        self.residencyCombobox.setItemText(7, QCoreApplication.translate("MainWindow", u"\U0001f332 Spruce Sea Port", None))
        self.residencyCombobox.setItemText(8, QCoreApplication.translate("MainWindow", u"\U0001f6b6Walking City", None))
        self.residencyCombobox.setItemText(9, QCoreApplication.translate("MainWindow", u"\U0001f3de\U0000fe0f Summitstead", None))
        self.residencyCombobox.setItemText(10, QCoreApplication.translate("MainWindow", u"\U0001f40d Latveria", None))
        self.residencyCombobox.setItemText(11, QCoreApplication.translate("MainWindow", u"\U0001f377 Kirtown", None))
        self.residencyCombobox.setItemText(12, QCoreApplication.translate("MainWindow", u"\u2744\ufe0f Snowtown", None))
        self.residencyCombobox.setItemText(13, QCoreApplication.translate("MainWindow", u"\U0001f41c Fort Ant", None))
        self.residencyCombobox.setItemText(14, QCoreApplication.translate("MainWindow", u"\U0001faa6 Midtown", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#c0c0bd;\">Personal Information</span></p></body></html>", None))
        self.femaleRadioButton.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.displayPictureDisplay.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">No Image Selected</span></p></body></html>", None))
        self.occupationCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Citizen", None))
        self.occupationCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Police", None))
        self.occupationCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Army", None))
        self.occupationCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Judge", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Occupation:", None))
        self.idNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TG-0000-000000-00", None))
        self.otherGenderRadioButton.setText(QCoreApplication.translate("MainWindow", u"Other (specify)", None))
        self.displayName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Minecraft Username", None))
#if QT_CONFIG(statustip)
        self.generateButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Generate ID", None))
#endif // QT_CONFIG(statustip)
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#c0c0bd;\">Display Picture</span></p></body></html>", None))
        self.reloadPreviewImage.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-style:italic; color:#cfcfcf;\">Filetypes supported: PNG, JPEG<br/>Must be 30*40 or multiples</span></p></body></html>", None))
        self.selectFileButton.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.preferNotSayRadioButton.setText(QCoreApplication.translate("MainWindow", u"Prefer not to say", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuID.setTitle(QCoreApplication.translate("MainWindow", u"ID", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuAboutTaigaIDGenerator.setTitle(QCoreApplication.translate("MainWindow", u"About Taiga ID Generator", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

