#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: example_1.py
@time: 2020/9/28 18:34
@desc: 简单的窗口调出
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 250)
    w.move(500, 500)
    w.setWindowTitle("hello")
    w.show()

    sys.exit(app.exec_())
