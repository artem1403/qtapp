# Расположу здесь функции, которые используются в кнопках как реакция на нажатие
from PyQt5.QtWidgets import QMessageBox

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()