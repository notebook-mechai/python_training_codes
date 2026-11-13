from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic # User Interface Compiler - uic
import sys

class UI_designer(QWidget):

    def __init__(self):
        super().__init__()
        uic.load_ui.loadUi("2/userInterface_eventHandling.ui", self)
        self.btn_push.clicked.connect(self.action_btn_push)

    def action_btn_push(self):
        self.lbl_result.setText(self.message.text())

   
app = QApplication(sys.argv)
window = UI_designer()
window.show()
sys.exit(app.exec())
