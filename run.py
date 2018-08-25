import sys
from PyQt5.QtWidgets import QApplication
from main import mainWindow

app = QApplication(sys.argv)
window = mainWindow()
sys.exit(app.exec_())
