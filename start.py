from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QInputDialog, QWidget, QApplication, QTabWidget, QLabel, QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView, QSpinBox, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLineEdit, QFormLayout, QHBoxLayout, QLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QDir, QObject, Qt, QThread, QTimer, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QGuiApplication, QCursor, QClipboard

import window_ui

class Window(window_ui):

    def __init__(self):
        super().__init__()
        self.ui = window_ui()
        self.ui.setupUi(self)

if __name__ == '__main__':
    global app, translator, window
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())