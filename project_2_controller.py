from PyQt5.QtWidgets import *
from project_2_view_main import *
from PyQt5 import QtGui

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.AlaskaButton.adjustSize()
        self.CaliforniaButton.adjustSize()
        self.ArizonaButton.adjustSize()
        self.ColoradoButton.adjustSize()
        self.TitleLabel.adjustSize()

        self.AlaskaButton.clicked.connect(lambda: self.alaska())
        self.CaliforniaButton.clicked.connect(lambda: self.california())
        self.ArizonaButton.clicked.connect(lambda: self.arizona())
        self.ColoradoButton.clicked.connect(lambda: self.colorado())
    def alaska(self):
        self.AlaskaPicture.setPixmap(QtGui.QPixmap("alaska.jpg"))
    def california(self):
        self.CaliforniaPicture.setPixmap(QtGui.QPixmap("california.jpg"))
    def arizona(self):
        self.ArizonaPicture.setPixmap(QtGui.QPixmap("arizona.jpg"))
    def colorado(self):
        self.ColoradoPicture.setPixmap(QtGui.QPixmap("colorado.jpg"))
