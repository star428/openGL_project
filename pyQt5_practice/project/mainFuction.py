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

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction

from childFuction import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("Function")

        self.statusBar()

        LineAct = QAction(QIcon(""), "Line", self)
        LineAct.setStatusTip('')
        LineAct.triggered.connect(self.childWindow_one)

        fileMenu.addAction(LineAct)

        BresenhamAct = QAction(QIcon(""), "Bresenham Line", self)
        BresenhamAct.setStatusTip("")
        BresenhamAct.triggered.connect(self.childWindow_two)

        fileMenu.addAction(BresenhamAct)

        self.setGeometry(1000, 1000, 500, 500)
        self.setWindowTitle("draw the graph")

    def childWindow_one(self):
        self.childOne = childWindowOne()
        self.childOne.show()

    def childWindow_two(self):
        self.childTwo = childWindowTwo()
        self.childTwo.show()
