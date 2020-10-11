#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: example_6.py
@time: 2020/10/6 18:18
@desc:
"""
import random
import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from time import sleep


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        pen = QPen(Qt.black, 5)
        qp.setPen(pen)
        size = self.size()

        for i in range(10):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)

            qp.drawPoint(x, y)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
