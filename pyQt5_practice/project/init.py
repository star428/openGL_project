#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: init.py
@time: 2020/9/28 22:17
@desc:
"""
import sys
from PyQt5.QtWidgets import QApplication
from mainFuction import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 每一个pyqt5应用都必须创建一个对象
    mainwindow = MainWindow()
    # 创建窗口
    mainwindow.show()
    # 展示窗口
    sys.exit(app.exec_())
    # 结束
