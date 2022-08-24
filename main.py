import webbrowser
import images

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.old_pos = None
        loadUi(".\\uiFiles\\LoginUi.ui", self)
        self.input_login.setMaxLength(64)
        self.input_password.setMaxLength(64)
        self.get_buttons()

    def get_buttons(self):
        self.GitHub.clicked.connect(lambda: webbrowser.open("https://github.com/xMedicago"))

    # вызывается при нажатии кнопки мыши
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = event.pos()

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    #  вызывается при закрытии приложения
    def closeEvent(self, event):
        msg = QMessageBox(self)
        msg.setWindowIcon(QIcon(".\\images\\icon.png"))
        msg.setWindowTitle("Уже уходите?)")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы уверены, что хотите закрыть приложение?")
        okButton = msg.addButton("Yes", QMessageBox.AcceptRole)
        msg.addButton("No", QMessageBox.RejectRole)

        msg.exec_()

        if msg.clickedButton() == okButton:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication([])

    login = Login()
    login.show()
    app.exec_()
