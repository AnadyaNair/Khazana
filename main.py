import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https:google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Previous', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)


app = QApplication(sys.argv)
QApplication.setApplicationName('Khazana Browser')
window = MainWindow()
app.exec_()
