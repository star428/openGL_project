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
from PyQt5.QtWidgets import QWidget


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
