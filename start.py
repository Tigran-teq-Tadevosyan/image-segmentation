from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QInputDialog, QWidget, QApplication, QTabWidget, QLabel, QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView, QSpinBox, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLineEdit, QFormLayout, QHBoxLayout, QLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QDir, QObject, Qt, QThread, QTimer, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QGuiApplication, QCursor, QClipboard

import sys

import window_ui
from main import prcessImage

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.__selectImagePath = None

    @pyqtSlot()
    def selectImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"Select Image", "","Select Image (*.jpg *jpeg)", options=options)
        self.__selectImagePath = fileName
        self.ui.ImagePath.setText(fileName)
    
    @pyqtSlot()
    def process(self):
        prcessImage(self.__selectImagePath,self.ui.MuSpinBox.value())

        pixmap = QPixmap('./result/result.jpg')
        self.ui.ImageDisplayLabel.setPixmap(pixmap)

        # Optional, resize window to image size
        self.resize(pixmap.width(),pixmap.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())