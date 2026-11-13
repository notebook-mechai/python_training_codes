from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("files/pro_icon.png"))
        self.setWindowTitle("first event")
        self.setGeometry(200,200,400,200)
        self.create_widgets()

    def create_widgets(self):
         # step 1
        hbox = QHBoxLayout()
        # step 2
        btn_push = QPushButton("Push Me")
        btn_push.clicked.connect(self.action_btn_push)
        self.message = QLineEdit(self)
        self.lbl_result = QLabel("default Text", self)
        # step 3
        hbox.addWidget(btn_push)
        hbox.addWidget(self.message)
        hbox.addWidget(self.lbl_result)
        # step 4
        self.setLayout(hbox)

    def action_btn_push(self):
        self.lbl_result.setText(self.message.text())



        
        


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
