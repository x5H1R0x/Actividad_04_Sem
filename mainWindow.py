from PySide2.QtWidgets import QMainWindow   
from ui_mainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)