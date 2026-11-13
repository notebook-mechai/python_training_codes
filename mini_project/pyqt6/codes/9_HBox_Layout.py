from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("files/pro_icon.png"))
        self.setWindowTitle("project")
        self.setGeometry(200,200,600,300)
        # +++++++++++++++++++++
        self.create_buttons()

    def create_buttons(self):
        # step 1
        hbox = QHBoxLayout()
        # step 2
        # hbox.addSpacing(50)
        btn1 = QPushButton("button1")
        btn2 = QPushButton("button2")
        btn3 = QPushButton("button3")
        # step 3
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        # step 4
        self.setLayout(hbox)

       

        


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
