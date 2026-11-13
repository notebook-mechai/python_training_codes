from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("files/pro_icon.png"))
        self.setWindowTitle("project")
        self.setGeometry(200,200,600,300)

        btn_start = QPushButton("start", self)
        # btn_start.move(10, 20)
        btn_start.setGeometry(10,20, 100, 25)
        btn_start.setStyleSheet('''
                                color: darkblue; 
                                font-weight: bold; 
                                font-size:14px
                            ''')
        btn_start.setIcon(QIcon("fire.png"))
        btn_start.setIconSize(QSize(18, 18))


        btn_menu = QPushButton("click me", self)
        btn_menu.setGeometry(10,50, 100, 25)
        menu = QMenu()
        menu.addAction("start_action_one")
        menu.addAction("start_action_two")
        menu.addAction("start_action_three")
        btn_menu.setMenu(menu)

        
       

        


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
