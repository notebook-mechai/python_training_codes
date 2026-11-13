from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu, QLineEdit
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("files/pro_icon.png"))
        self.setWindowTitle("project")
        self.setGeometry(200,200,600,300)
        # ++++++++++++++++++++++++++++++++++++++++
        lbl_fn = QLabel("First name:", self)
        lbl_fn.setFont(QFont("Tahoma", 12))
        lbl_fn.move(10, 10)
        # ++++++++++++++++++++++++++++++++++++++++
        le_fn = QLineEdit(self)
        le_fn.setGeometry(100,10, 200, 25)
        le_fn.setPlaceholderText("please enter your name")
        # le_fn.move(100, 10)
        # le_fn.setText("ddd")
        # le_fn.setEnabled(False)
        # le_fn.setEnabled(True)
        # le_fn.setEchoMode(QLineEdit.EchoMode.Password)

       

        


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
