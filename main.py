from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5.uic import loadUi
import images


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.old_pos = None
        loadUi(".\\uiFiles\\LoginUi.ui", self)

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


if __name__ == '__main__':
    app = QApplication([])

    login = Login()
    login.show()
    app.exec_()
