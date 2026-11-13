from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../files/pro_icon.png"))
        self.setWindowTitle("project")
        self.setGeometry(200,200,600,300)
        
        label = QLabel(self)
        mini_movie = QMovie("../files/new.gif")
        label.setMovie(mini_movie)
        mini_movie.start()

        


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
