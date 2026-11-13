from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("files/pro_icon.png"))
        self.setWindowTitle("project")
        self.setGeometry(200,200,600,300)
        
        self.create_buttons()

    def create_buttons(self):
        # step 1
        vbox = QVBoxLayout()
        # step 2
        # vbox.addSpacing(50)
        btn1 = QPushButton("button_1")
        btn2 = QPushButton("button_2")
        btn3 = QPushButton("button_3")
        # step 3
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        # vbox.addStretch() # Very Important ( remove auto spave for between Widget)
        # step 4
        self.setLayout(vbox)

       

        


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
