#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: example_2.py
@time: 2020/9/28 20:13
@desc:
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QWidget


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

        BresenhamAct = QAction(QIcon(""),"Bresenham Line",self)
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

class childWindowOne(QWidget):
    def __init__(self):
        super(childWindowOne, self).__init__()

        self.setGeometry(500, 500, 600, 600)
        self.setWindowTitle("DDA Line Setting")

class childWindowTwo(QWidget):
    def __init__(self):
        super(childWindowTwo, self).__init__()

        self.setGeometry(500, 500, 600, 600)
        self.setWindowTitle("Bresenham Line Setting")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
