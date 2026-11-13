from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel
from PyQt6.QtGui import QIcon

import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowIcon(QIcon("../files/pro_icon.png"))
window.setWindowTitle("smile")
window.setGeometry(200,200,600,300)
# window.setWindowOpacity(0.9)

window.show()

sys.exit(app.exec())
