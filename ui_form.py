# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(598, 428)
        main.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;")
        self.label = QLabel(main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(116, 40, 201, 51))
        self.label.setStyleSheet(u" color: #333333; \n"
"font-size: 35px; \n"
"padding : 4px;\n"
"font-weight: bold; \n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_2 = QLabel(main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(94, 92, 191, 41))
        self.label_2.setStyleSheet(u" color: #333333; \n"
"font-size: 20px; \n"
"padding : 4px;\n"
"font-weight: semi-bold; \n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_3 = QLabel(main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 43, 55, 51))
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 0px;")
        self.responce = QLabel(main)
        self.responce.setObjectName(u"responce")
        self.responce.setGeometry(QRect(397, 49, 160, 160))
        self.responce.setStyleSheet(u"\n"
"border-radius: 10px;")
        self.input = QLineEdit(main)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(60, 180, 251, 45))
        self.input.setAutoFillBackground(False)
        self.input.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f9f9f9;\n"
"    color: #333333;\n"
"    border: 2px solid #666666;\n"
"    padding: 10px;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 18px;\n"
"    border-radius: 8px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #444444;\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #007bff;\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"}\n"
"")
        self.pushButton = QPushButton(main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 334, 131, 41))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"    background-color: #007bff;;\n"
"    color: white;\n"
"    font: bold 18px;\n"
"    padding: 8px 12px;\n"
"    border: 2px solid #0056b3;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"    border-color: #003366;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003366;  \n"
"    border-color: #001a33;\n"
"}\n"
"")
        self.colorbutton = QPushButton(main)
        self.colorbutton.setObjectName(u"colorbutton")
        self.colorbutton.setGeometry(QRect(400, 260, 160, 35))
        self.colorbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorbutton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 13px;\n"
"    background-color: #44CCCC;\n"
"    color: white;\n"
"    font: bold 18px;\n"
"    padding-left: 28px;\n"
"    padding-right: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    border: 1px solid #003366;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3399FF;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #3399FF;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #007BBB;\n"
"}\n"
"\n"
"QPushButton#downloadButton {\n"
"    background-color: #007bff;\n"
"}\n"
"\n"
"QPushButton#downloadButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"QPushButton#downloadButton:checked {\n"
"    background-color: #17a2b8;\n"
"}\n"
"")
        self.warning = QLabel(main)
        self.warning.setObjectName(u"warning")
        self.warning.setGeometry(QRect(180, 450, 191, 20))
        self.label_4 = QLabel(main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 578, 408))
        self.label_4.setStyleSheet(u"background-color: rgb(233, 246, 240);\n"
"border-radius: 25px;")
        self.label_5 = QLabel(main)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(378, 24, 198, 379))
        self.label_5.setStyleSheet(u"border-radius: 15px;\n"
"background-color: #00288A;")
        self.pushButton_2 = QPushButton(main)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(400, 326, 161, 31))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 13px;\n"
"    background-color: #FF9B05;\n"
"    color: white;\n"
"    font: bold 17px;\n"
"    padding-left: 20px;\n"
"    padding-right: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 7px;\n"
"    border: 1px solid #003366;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FF8903; \n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #17a2b8;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FF7D00; \n"
"}\n"
"\n"
"QPushButton#downloadButton {\n"
"    background-color: #007bff;\n"
"}\n"
"\n"
"QPushButton#downloadButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"QPushButton#downloadButton:checked {\n"
"    background-color: #17a2b8;\n"
"}\n"
"")
        self.label_7 = QLabel(main)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(414, 327, 30, 30))
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.label_8 = QLabel(main)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(407, 263, 30, 30))
        self.label_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.input_2 = QLineEdit(main)
        self.input_2.setObjectName(u"input_2")
        self.input_2.setGeometry(QRect(60, 252, 251, 45))
        self.input_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f9f9f9;\n"
"    color: #333333;\n"
"    border: 2px solid #666666;\n"
"    padding: 10px;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 18px;\n"
"    border-radius: 8px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #444444;\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #007bff;\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"}\n"
"")
        self.Warning = QLabel(main)
        self.Warning.setObjectName(u"Warning")
        self.Warning.setGeometry(QRect(391, 220, 171, 21))
        self.Warning.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.error = QLabel(main)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(148, 304, 131, 21))
        self.error.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: #FF6347;\n"
"font-family: Arial, sans-serif;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"")
        self.download = QLabel(main)
        self.download.setObjectName(u"download")
        self.download.setGeometry(QRect(406, 366, 161, 21))
        self.download.setStyleSheet(u" background-color: rgba(255, 255, 255, 0);\n"
"  color: #CCCCCC;\n"
" ")
        self.label_6 = QLabel(main)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 386, 191, 41))
        self.label_6.setStyleSheet(u" color: #333333; \n"
"font-size: 14px; \n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.input.raise_()
        self.pushButton.raise_()
        self.warning.raise_()
        self.label_5.raise_()
        self.pushButton_2.raise_()
        self.label_7.raise_()
        self.responce.raise_()
        self.colorbutton.raise_()
        self.label_8.raise_()
        self.input_2.raise_()
        self.Warning.raise_()
        self.error.raise_()
        self.download.raise_()
        self.label_6.raise_()

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.label.setText(QCoreApplication.translate("main", u"QR Master", None))
        self.label_2.setText(QCoreApplication.translate("main", u"QR Code Generator", None))
        self.label_3.setText("")
        self.responce.setText("")
        self.input.setPlaceholderText(QCoreApplication.translate("main", u"Enter Text...", None))
        self.pushButton.setText(QCoreApplication.translate("main", u"Generate", None))
        self.colorbutton.setText(QCoreApplication.translate("main", u"Select Color", None))
        self.warning.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("main", u"Download", None))
        self.label_7.setText("")
        self.label_8.setText("")
        self.input_2.setPlaceholderText(QCoreApplication.translate("main", u"Enter URL...", None))
        self.Warning.setText("")
        self.error.setText("")
        self.download.setText("")
        self.label_6.setText(QCoreApplication.translate("main", u"Coded by : Zain Jamshaid", None))
    # retranslateUi

