from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt6.QtGui import QIcon

import sys

app = QApplication(sys.argv)
# window = QWidget()
window = QMainWindow()

window.setWindowIcon(QIcon("../files/pro_icon.png"))
window.setWindowTitle("--windows title--")
window.setGeometry(200,200,600,300)
window.setWindowOpacity(0.9)
window.statusBar().showMessage("Welcome to PyQt6")
window.menuBar().addMenu("File")
window.menuBar().addMenu("view")
window.show()

sys.exit(app.exec())
