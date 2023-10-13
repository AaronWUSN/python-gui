import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("First Try")
		xsize = 800
		ysize = 600
		self. setGeometry(0,0,xsize,ysize)
	
app = QApplication(sys.argv)
	
window = MainWindow()
window.show()
	
app.exec()	
