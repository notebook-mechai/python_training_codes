from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../files/pro_icon.png"))
        self.setWindowTitle("---")
        self.setGeometry(200,200,600,300)


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())






