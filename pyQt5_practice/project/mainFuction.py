#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: mainFuction.py
@time: 2020/9/28 22:19
@desc:
"""
# 两个方向，一个是继续寻找暂停，另一个是从matplotlib中重写，由于框架已经就绪
# 再次重写较为简单
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import (QMainWindow, QAction)

from childFuction import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.position = None
        self.points = []
        # 设置标志位此时达到不同算法的切换
        self.signal = 0
        self.initUI()
        # 直接在主函数中初始化函数

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("Function")

        self.statusBar()
        # 增加第一个菜单栏下的工具
        LineAct = QAction(QIcon(""), "Line", self)
        LineAct.setStatusTip('')
        LineAct.triggered.connect(self.childWindow_one)

        fileMenu.addAction(LineAct)
        # 增加第二个菜单栏下的工具
        BresenhamAct = QAction(QIcon(""), "Bresenham Line", self)
        BresenhamAct.setStatusTip("")
        BresenhamAct.triggered.connect(self.childWindow_two)

        fileMenu.addAction(BresenhamAct)

        # 鼠标控制
        # self.mouseControl()
        # 鼠标控制结束

        self.resize(600, 500)
        self.center()
        self.setWindowTitle("draw the graph")

    # def mouseControl(self):
    #     x = 0
    #     y = 0
    #
    #     self.text = "x: {0},  y: {1}".format(x, y)
    #     self.label = QLabel(self.text, self)
    #     self.label.move(-100, -100)
    #     self.setMouseTracking(True)
    #
    # def mouseMoveEvent(self, e):
    #     重写鼠标事件
    #     size = self.size()
    # x = e.x() - size.width() / 2
    # y = size.height() / 2 - e.y()
    #
    # text = "x: {0},  y: {1}".format(x, y)
    # self.statusBar().showMessage(text)

    def paintEvent(self, event):
        # 重写画笔事件
        qp = QPainter()
        qp.begin(self)
        self.drawCoordinate(qp)
        if self.signal == 1:
            self.drawDDALine(qp)

        qp.end()

    def center(self):
        # 使屏幕居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def childWindow_one(self):
        # 子窗口事件，同时连接了信号槽
        self.childOne = childWindowOne()
        self.childOne.show()
        self.childOne._signal.connect(self.getMessageOne)
        self.signal = 1

    def childWindow_two(self):
        self.childTwo = childWindowTwo()
        self.childTwo.show()

    def getMessageOne(self, x0, y0, xEnd, yEnd):
        # 加入第一个事件的事件槽
        self.position = x0, y0, xEnd, yEnd

    def drawCoordinate(self, qp):
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        qp.setPen(pen)
        size = self.size()
        centerPoint = (size.width() / 2, size.height() / 2)
        # 坐标轴的线
        qp.drawLine(0, size.height() / 2, size.width(), size.height() / 2)
        qp.drawLine(size.width() / 2, 0, size.width() / 2, size.height())

        # 坐标轴的小轴和字
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        qp.setFont(QFont('Courier New', 5))
        qp.setPen(pen)
        for xInc in range(10, int(centerPoint[0]), 10):
            x = centerPoint[0]
            y = centerPoint[1]

            if xInc % 100 == 0:
                qp.drawText(x + xInc, y + 10, str(xInc))
                qp.drawText(x - xInc, y + 10, str(xInc))
                qp.drawLine(x + xInc, y, x + xInc, y - 10)
                qp.drawLine(x - xInc, y, x - xInc, y - 10)

            qp.drawLine(x + xInc, y, x + xInc, y - 5)
            qp.drawLine(x - xInc, y, x - xInc, y - 5)

        for yInc in range(10, int(centerPoint[1]), 10):
            x = centerPoint[0]
            y = centerPoint[1]
            if yInc % 100 == 0:
                qp.drawText(x - 20, y + yInc, str(yInc))
                qp.drawText(x - 20, y - yInc, str(yInc))
                qp.drawLine(x, y + yInc, x + 10, y + yInc)
                qp.drawLine(x, y - yInc, x + 10, y - yInc)

            qp.drawLine(x, y + yInc, x + 5, y + yInc)
            qp.drawLine(x, y - yInc, x + 5, y - yInc)

    def drawDDALine(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        size = self.size()

        if self.position is not None:
            self.points = DDALine(self.position, size)
            for point in self.points:
                qp.drawPoint(point[0], point[1])
            # self.position = None

# 下面定义为外置代码
def changeCoordinate(position, windowSize):
    return (position[0] + windowSize.width() / 2,
            windowSize.height() / 2 - position[1])


def round(num):
    return int(num + 0.5)


def DDALine(position, windowSize):
    # x, y = changeCoordinate(position, windowSize)
    # qp.drawPoint(x, y)
    points = []
    dx = abs(position[0] - position[2])
    dy = abs(position[1] - position[3])

    x = position[0]
    y = position[1]

    if dx > dy:
        steps = int(dx)
    else:
        steps = int(dy)

    x_increase = dx / steps
    y_increase = dy / steps

    out_x, out_y = changeCoordinate((x, y), windowSize)
    points.append((out_x, out_y))
    for step in range(steps):
        x += x_increase
        y += y_increase

        out_x, out_y = changeCoordinate((x, y), windowSize)
        points.append((out_x, out_y))

    return points
