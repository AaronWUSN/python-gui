import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

def MainWindow():
	app = QApplication([])
	window = QWidget()
	xsize = 1000
	ysize = 800
	window.setGeometry(0,0,xsize,ysize)
	window.setWindowTitle("First Try")

	window.show()
	app.exec()
	
MainWindow()
