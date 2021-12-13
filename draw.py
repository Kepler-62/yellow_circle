import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from ui import Ui_MainWindow

import random


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
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
        self.painter.setBrush(QColor(random.choice(range(256)), random.choice(range(256)), random.choice(range(256))))
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
