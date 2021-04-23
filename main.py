import sys
from PyQt5.QtWidgets import *
from button_handlers import *


class PyQtLayout(QWidget):
	def __init__(self):
		super().__init__()
		self.UI()

	def UI(self):
		layout = QVBoxLayout()
		top_button = QPushButton('Top')
		top_button.clicked.connect(on_button_clicked)
		layout.addWidget(top_button)
		layout.addWidget(QPushButton('Bottom'))
		self.setLayout(layout)
		self.show()


def main():
	app = QApplication(sys.argv)
	app.setStyle('Fusion')
	ex = PyQtLayout()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()