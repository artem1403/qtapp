from PyQt5.QtWidgets import *
from button_handlers import *

app = QApplication([])
app.setStyle('Fusion')
# app.setStyleSheet("QPushButton { margin: 10px; }")
window = QWidget()
layout = QVBoxLayout()
top_button = QPushButton('Top')
top_button.clicked.connect(on_button_clicked)
layout.addWidget(top_button)
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec()