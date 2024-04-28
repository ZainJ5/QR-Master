import sys
import os
import requests
import rc_img
from PySide6.QtCore import QFile
from PySide6.QtCore import QStandardPaths
from PySide6.QtWidgets import QApplication, QWidget,QColorDialog
from PySide6.QtGui import QPixmap,QIcon
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from ui_form import Ui_main

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_main()
        self.ui.setupUi(self)
        icon=(":/img/Images/icon1.png")
        self.setWindowIcon(QIcon(icon));
        self.setWindowTitle("QR Master")
        self.setFixedSize(598, 428)
        flags = self.windowFlags()
        flags |= Qt.WindowMinimizeButtonHint
        self.setWindowFlags(flags)

        photo = QPixmap(":/img/Images/LOGO.png")
        h = self.ui.label_3.height()
        w = self.ui.label_3.width()
        self.ui.label_3.setPixmap(photo.scaled(w, h))


        photo1 = QPixmap(":/img/Images/final.png")
        h1 = self.ui.label_7.height()
        w1 = self.ui.label_7.width()
        self.ui.label_7.setPixmap(photo1.scaled(w1, h1))

        photo2 = QPixmap(":/img/Images/color.png")
        h2 = self.ui.label_8.height()
        w2 = self.ui.label_8.width()
        self.ui.label_8.setPixmap(photo2.scaled(w2, h2))

        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_DownloadButton_clicked)
        self.ui.input.textChanged.connect(self.updateInput2State)
        self.ui.input_2.textChanged.connect(self.updateInputState)
        self.ui.colorbutton.clicked.connect(self.openColorPicker)
        self.color_string='FFFFFF'

    def openColorPicker(self):
        color = QColorDialog.getColor()
        if color.isValid():
           self.color_string = color.name(QColor.HexRgb)[1:]

    def updateInputState(self):
        self.ui.error.setText("  ")
        self.ui.download.setText("")
        self.ui.Warning.setText("")
        self.ui.responce.clear()
        if self.ui.input_2.text():
                self.ui.input.setReadOnly(True)
                self.ui.input.setEnabled(False)
        else:
            self.ui.input.setReadOnly(False)
            self.ui.input.setEnabled(True)
    def updateInput2State(self):
        self.ui.download.setText("")
        self.ui.Warning.setText("")
        self.ui.error.setText("  ")
        self.ui.responce.clear()
        if self.ui.input.text():
            self.ui.input_2.setReadOnly(True)
            self.ui.input_2.setEnabled(False)
        else:
            self.ui.input_2.setReadOnly(False)
            self.ui.input_2.setEnabled(True)

    def on_pushButton_clicked(self):
        check=False
        check1=False
        self.url = self.ui.input_2.text() or self.ui.input.text()
        if not self.ui.input.text() or (not self.ui.input.text().startswith("http://") and not self.ui.input.text().startswith("www") and not self.ui.input.text().startswith("https://")):
            check=True
        else:
            self.ui.error.setText("Invalid text")

        if not self.ui.input_2.text() or self.ui.input_2.text().startswith("http://") or self.ui.input_2.text().startswith("www") or self.ui.input_2.text().startswith("https://"):
            check1=True
        else:
            self.ui.error.setText("Invalid URL")

        if check and check1:
            string = 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + self.url + '&bgcolor=' + self.color_string
            self.r = requests.get(string)
            if self.r.status_code == 200:
                self.ui.Warning.setText("QR CODE successfully generated")
                self.ui.Warning.setStyleSheet("QLabel {color: #00FF00;"
                                              "background-color: rgba(255, 255, 255, 0);}")
                pixmap = QPixmap()
                pixmap.loadFromData(self.r.content)
                h1 = self.ui.responce.height()
                w1 = self.ui.responce.width()
                self.ui.responce.setPixmap(pixmap.scaled(w1, h1))
            else:
                self.ui.Warning.setText("    Error generating QR code")
                self.ui.Warning.setStyleSheet("QLabel {color: Red;"
                                              "background-color: rgba(255, 255, 255, 0);"
                                              "text-align: center;}")

    def on_DownloadButton_clicked(self):
      if self.r.status_code == 200:
        filename = "QRMASTER-" + self.url + ".png"
        download_dir = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        filepath = os.path.join(download_dir, filename)
        with open(filepath, 'wb') as file:
          if file :
            self.ui.download.setText("QR CODE successfully stored")
            file.write(self.r.content)
          else:
            self.ui.download.setText("Error downloading QR CODE")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
