#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: childFuction.py
@time: 2020/9/28 22:25
@desc:
"""
from PyQt5.QtWidgets import (QWidget, QGridLayout, QLabel,
                             QLineEdit, QPushButton, QDesktopWidget)
from PyQt5 import QtCore


# 后面的每一个子类没有本质的区别，只有一些不同
class childWindowOne(QWidget):
    # 对于每一个实例来讲都相同，不会因为实例的改变而改变
    _signal = QtCore.pyqtSignal(float, float, float, float)

    def __init__(self):
        super(childWindowOne, self).__init__()

        self.initUI()

    def initUI(self):
        # 创建4个标签
        xBegin = QLabel("xBegin")
        yBegin = QLabel("yBegin")
        xEnd = QLabel("xEnd")
        yEnd = QLabel("yEnd")
        # 创建两个按钮
        btnYes = QPushButton("yes", self)
        btnYes.resize(btnYes.sizeHint())
        btnYes.clicked.connect(self.setMessage)
        btnNo = QPushButton("no", self)
        btnNo.clicked.connect(self.close)
        btnNo.resize(btnNo.sizeHint())

        # 增加文本框
        self.xBeginEdit = QLineEdit()
        self.yBeginEdit = QLineEdit()
        self.xEndEdit = QLineEdit()
        self.yEndEdit = QLineEdit()
        # 初始化排版
        grid = QGridLayout()
        grid.setSpacing(10)
        # 设定各自的位置
        grid.addWidget(xBegin, 0, 0)
        grid.addWidget(self.xBeginEdit, 0, 1)
        grid.addWidget(yBegin, 0, 2)
        grid.addWidget(self.yBeginEdit, 0, 3)

        grid.addWidget(xEnd, 1, 0)
        grid.addWidget(self.xEndEdit, 1, 1)
        grid.addWidget(yEnd, 1, 2)
        grid.addWidget(self.yEndEdit, 1, 3)

        grid.addWidget(btnYes, 2, 1)
        grid.addWidget(btnNo, 2, 3)

        self.setLayout(grid)

        self.resize(500, 200)
        self.center()
        self.setWindowTitle("DDA Line Setting")

    def center(self):
        # 使屏幕居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setMessage(self):
        x0 = float(self.xBeginEdit.text())
        y0 = float(self.yBeginEdit.text())
        xEnd = float(self.xEndEdit.text())
        yEnd = float(self.yEndEdit.text())
        self._signal.emit(x0, y0, xEnd, yEnd)
        self.close()


class childWindowTwo(QWidget):
    _signal = QtCore.pyqtSignal(float, float, float, float)

    def __init__(self):
        super(childWindowTwo, self).__init__()

        self.initUI()

    def initUI(self):
        xBegin = QLabel("xBegin")
        yBegin = QLabel("yBegin")
        xEnd = QLabel("xEnd")
        yEnd = QLabel("yEnd")
        # 创建两个按钮
        btnYes = QPushButton("yes", self)
        btnYes.resize(btnYes.sizeHint())
        btnYes.clicked.connect(self.setMessage)
        btnNo = QPushButton("no", self)
        btnNo.clicked.connect(self.close)
        btnNo.resize(btnNo.sizeHint())

        # 增加文本框
        self.xBeginEdit = QLineEdit()
        self.yBeginEdit = QLineEdit()
        self.xEndEdit = QLineEdit()
        self.yEndEdit = QLineEdit()
        # 初始化排版
        grid = QGridLayout()
        grid.setSpacing(10)
        # 设定各自的位置
        grid.addWidget(xBegin, 0, 0)
        grid.addWidget(self.xBeginEdit, 0, 1)
        grid.addWidget(yBegin, 0, 2)
        grid.addWidget(self.yBeginEdit, 0, 3)

        grid.addWidget(xEnd, 1, 0)
        grid.addWidget(self.xEndEdit, 1, 1)
        grid.addWidget(yEnd, 1, 2)
        grid.addWidget(self.yEndEdit, 1, 3)

        grid.addWidget(btnYes, 2, 1)
        grid.addWidget(btnNo, 2, 3)

        self.setLayout(grid)

        self.resize(500, 200)
        self.center()
        self.setWindowTitle("Bresenham Line Setting")

    def center(self):
        # 使屏幕居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setMessage(self):
        x0 = float(self.xBeginEdit.text())
        y0 = float(self.yBeginEdit.text())
        xEnd = float(self.xEndEdit.text())
        yEnd = float(self.yEndEdit.text())
        self._signal.emit(x0, y0, xEnd, yEnd)
        self.close()


class childWindowThree(QWidget):
    _signal = QtCore.pyqtSignal(float, float, float)

    def __init__(self):
        super(childWindowThree, self).__init__()

        self.initUI()

    def initUI(self):
        x = QLabel("x")
        y = QLabel("y")
        r = QLabel("r")
        # 创建两个按钮
        btnYes = QPushButton("yes", self)
        btnYes.resize(btnYes.sizeHint())
        btnYes.clicked.connect(self.setMessage)
        btnNo = QPushButton("no", self)
        btnNo.clicked.connect(self.close)
        btnNo.resize(btnNo.sizeHint())

        # 增加文本框
        self.xEdit = QLineEdit()
        self.yEdit = QLineEdit()
        self.rEdit = QLineEdit()
        # 初始化排版
        grid = QGridLayout()
        grid.setSpacing(10)
        # 设定各自的位置
        grid.addWidget(x, 0, 0)
        grid.addWidget(self.xEdit, 0, 1)
        grid.addWidget(y, 0, 2)
        grid.addWidget(self.yEdit, 0, 3)

        grid.addWidget(r, 1, 0)
        grid.addWidget(self.rEdit, 1, 1)

        grid.addWidget(btnYes, 2, 1)
        grid.addWidget(btnNo, 2, 3)

        self.setLayout(grid)

        self.resize(500, 200)
        self.center()
        self.setWindowTitle("Circle Setting")

    def center(self):
        # 使屏幕居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setMessage(self):
        x = float(self.xEdit.text())
        y = float(self.yEdit.text())
        r = float(self.rEdit.text())
        self._signal.emit(x, y, r)
        self.close()


class childWindowFour(QWidget):
    _signal = QtCore.pyqtSignal(float, float, float, float)

    def __init__(self):
        super(childWindowFour, self).__init__()

        self.initUI()

    def initUI(self):
        x = QLabel("x")
        y = QLabel("y")
        rx = QLabel("rx")
        ry = QLabel("ry")
        # 创建两个按钮
        btnYes = QPushButton("yes", self)
        btnYes.resize(btnYes.sizeHint())
        btnYes.clicked.connect(self.setMessage)
        btnNo = QPushButton("no", self)
        btnNo.clicked.connect(self.close)
        btnNo.resize(btnNo.sizeHint())

        # 增加文本框
        self.xEdit = QLineEdit()
        self.yEdit = QLineEdit()
        self.rxEdit = QLineEdit()
        self.ryEdit = QLineEdit()
        # 初始化排版
        grid = QGridLayout()
        grid.setSpacing(10)
        # 设定各自的位置
        grid.addWidget(x, 0, 0)
        grid.addWidget(self.xEdit, 0, 1)
        grid.addWidget(y, 0, 2)
        grid.addWidget(self.yEdit, 0, 3)

        grid.addWidget(rx, 1, 0)
        grid.addWidget(self.rxEdit, 1, 1)
        grid.addWidget(ry, 1, 2)
        grid.addWidget(self.ryEdit, 1, 3)

        grid.addWidget(btnYes, 2, 1)
        grid.addWidget(btnNo, 2, 3)

        self.setLayout(grid)

        self.resize(500, 200)
        self.center()
        self.setWindowTitle("Ellipse Line Setting")

    def center(self):
        # 使屏幕居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setMessage(self):
        x = float(self.xEdit.text())
        y = float(self.yEdit.text())
        rx = float(self.rxEdit.text())
        ry = float(self.ryEdit.text())
        self._signal.emit(x, y, rx, ry)
        self.close()
