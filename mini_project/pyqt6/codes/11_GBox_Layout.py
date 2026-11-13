from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
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
        grid_box = QGridLayout()
        # step 2
        # vbox.addSpacing(50)
        btn1 = QPushButton("button_1")
        btn2 = QPushButton("button_2")
        btn3 = QPushButton("button_3")
        btn4 = QPushButton("button_4")
        # step 3
        # grid_box.addWidget(NAME_OF_WIDGET, ROW_NUMBER, COLUMN_NUMBER)
        grid_box.addWidget(btn1, 0,0)
        grid_box.addWidget(btn2, 0,1)
        grid_box.addWidget(btn3, 1,0)
        grid_box.addWidget(btn4, 1,1)
        # grid_box.addStretch() # Very Important ( remove auto spave for between Widget)
        # step 4
        self.setLayout(grid_box)

       

        


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
