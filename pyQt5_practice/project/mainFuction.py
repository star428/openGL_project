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
# 利用example_9中的嵌入
import time

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import (QMainWindow, QAction)

from childFuction import *
from DDA_Line import DDALine
from Breseham_Line import BresehamLine
from circle import Circle
from ellipse import Ellipse


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 接受信息
        self.position = None
        # 输出的所有点
        self.points = []
        # 将要输出到屏幕上的点
        self.outPoints = []
        # 设置标志位此时达到不同算法的切换
        self.signal = 0
        # 表示此时将要加入到输出队列的下一个点
        self.index = 0
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

        CircleAct = QAction(QIcon(""), "circle", self)
        CircleAct.setStatusTip("")
        CircleAct.triggered.connect(self.childWindow_three)

        fileMenu.addAction(CircleAct)

        EllipseAct = QAction(QIcon(""), "Ellipse", self)
        EllipseAct.setStatusTip("")
        EllipseAct.triggered.connect(self.childWindow_four)

        fileMenu.addAction(EllipseAct)

        # 鼠标控制
        # self.mouseControl()
        # 鼠标控制结束

        # 刷新控制
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.repaint)
        self.timer.start(25)
        # 刷新控制结束，控制秒数为1秒，上面的单位是毫秒计时

        self.resize(800, 600)
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
        if self.signal == 2:
            self.drawBresehamLine(qp)
        if self.signal == 3:
            self.drawCircle(qp)
        if self.signal == 4:
            self.drawEllipse(qp)

        qp.end()

    def center(self):
        # 使屏幕居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 在此处改主窗口事件
    def childWindow_one(self):
        # 子窗口事件，同时连接了信号槽
        self.childOne = childWindowOne()
        self.childOne.show()

        self.position = None
        self.points = None
        self.signal = 1
        self.outPoints = []
        self.index = 0

        self.childOne._signal.connect(self.getMessageOne)

    def childWindow_two(self):
        self.childTwo = childWindowTwo()
        self.childTwo.show()

        self.position = None
        self.points = None
        self.signal = 2
        self.outPoints = []
        self.index = 0

        self.childTwo._signal.connect(self.getMessageTwo)

    def childWindow_three(self):
        self.childThree = childWindowThree()
        self.childThree.show()

        self.position = None
        self.points = None
        self.signal = 3
        self.outPoints = []
        self.index = 0

        self.childThree._signal.connect(self.getMessageThree)

    def childWindow_four(self):
        self.childFour = childWindowFour()
        self.childFour.show()

        self.position = None
        self.points = None
        self.signal = 4
        self.outPoints = []
        self.index = 0

        self.childFour._signal.connect(self.getMessageFour)

    # 在此处定义接受信息的信号槽
    def getMessageOne(self, x0, y0, xEnd, yEnd):
        # 加入第一个事件的事件槽
        self.position = x0, y0, xEnd, yEnd

    def getMessageTwo(self, x0, y0, xEnd, yEnd):
        self.position = x0, y0, xEnd, yEnd

    def getMessageThree(self, x, y, r):
        self.position = x, y, r

    def getMessageFour(self, x, y, rx, ry):
        self.position = x, y, rx, ry

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
            if self.index < len(self.points):
                self.outPoints.append(self.points[self.index])
                self.index += 1
            # 用index调控每一次要输出的数目
        for outPoint in self.outPoints:
            qp.drawPoint(outPoint[0], outPoint[1])
            # self.position = None

    def drawBresehamLine(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        size = self.size()

        if self.position is not None:
            self.points = BresehamLine(self.position, size)
            if self.index < len(self.points):
                self.outPoints.append(self.points[self.index])
                self.index += 1
            # 用index调控每一次要输出的数目
        for outPoint in self.outPoints:
            qp.drawPoint(outPoint[0], outPoint[1])
            # self.position = None

    def drawCircle(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        size = self.size()

        if self.position is not None:
            self.points = Circle(self.position, size)
            if self.index < len(self.points):
                self.outPoints.append(self.points[self.index])
                self.index += 1
            # 用index调控每一次要输出的数目
        for outPoint in self.outPoints:
            qp.drawPoint(outPoint[0], outPoint[1])
            # self.position = None

    def drawEllipse(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        size = self.size()

        if self.position is not None:
            self.points = Ellipse(self.position, size)
            if self.index < len(self.points):
                self.outPoints.append(self.points[self.index])
                self.index += 1
            # 用index调控每一次要输出的数目
        for outPoint in self.outPoints:
            qp.drawPoint(outPoint[0], outPoint[1])
            # self.position = None

# 下面定义为外置代码
