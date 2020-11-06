#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: example_7.py
@time: 2020/10/7 9:50
@desc:
"""
# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In the example, we draw randomly 1000 red points 
on the window.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QTimer
import sys, random


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.startBtn = QPushButton("开始")
        self.startBtn.clicked.connect(self.startTimer)
        self.startBtn.move(200,200)


        # 救命的神级代码
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.repaint)
        self.timer.start(1000)
        ##################
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        pen = QPen(Qt.red, 5)
        qp.setPen(pen)
        size = self.size()

        for i in range(100):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)

    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
