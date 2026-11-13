from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../files/pro_icon.png"))
        self.setWindowTitle("project")
        self.setGeometry(200,200,600,300)
        # label_02 = QLabel(self)
        # label_02.setText("lastname:")

        lbl_fn = QLabel("First name:", self)
        lbl_fn.setFont(QFont("Tahoma", 12))
        lbl_fn.move(10, 10)
        # +++++++++++++++++++++++++++++++++++++++
        lbl_ln = QLabel("Last name:", self)
        lbl_ln.setFont(QFont("Tahoma", 12))
        lbl_ln.move(10, 40)
        # +++++++++++++++++++++++++++++++++++++++
        lbl_ni = QLabel("National id:", self)
        lbl_ni.move(10, 70)
        lbl_ni.setStyleSheet("color: darkblue; font-size:18px; font-family: arial")
        # +++++++++++++++++++++++++++++++++++++++

        


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
