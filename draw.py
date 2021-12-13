import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.flag = False
        self.painter = QPainter()
        self.pushButton.clicked.connect(self.drawf)

    def paintEvent(self, event):
        if self.flag is True:
            self.painter.begin(self)
            self.draw()
            self.painter.end()
            self.flag = False

    def draw(self):
        self.painter.setBrush(QColor('yellow'))
        size = random.randint(10, 400)
        x0, y0 = 250, 200
        self.painter.drawEllipse(x0 - size // 2, y0 - size // 2, size, size)

    def drawf(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
