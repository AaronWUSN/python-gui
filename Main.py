import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		NewGame = QPushButton(text = "New Game")
		LoadGame = QPushButton(text = "Load Game")
		box = QVBoxLayout()
		box.addWidget(NewGame)
		box.addWidget(LoadGame)
		box.setAlignment(Qt.AlignVCenter)
		self.setLayout(box)
		self.setGeometry(100,100,800,600)
		self.setWindowTitle("First Try")
		self.show()
		
	
app = QApplication(sys.argv)
	
window = MainWindow()
window.show()
	
app.exec()	
