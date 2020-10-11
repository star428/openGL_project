#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: example_9.py
@time: 2020/10/11 9:32
@desc:
"""
import numpy as np
import sys
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
# 使用 matplotlib中的FigureCanvas (在使用 Qt5 Backends中 FigureCanvas继承自QtWidgets.QWidget)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QTimer
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class App(QWidget):
    def __init__(self, parent=None):
        # 父类初始化方法
        super(App, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('动态演示')
        self.setWindowIcon(QIcon('电力图标.jpg'))
        self.setWindowIcon(QIcon('2345_image_file_copy_1.jpg'))
        self.setFixedSize(1200, 700)
        self.setMinimumSize(1200, 700)
        self.setMaximumSize(1200, 700)
        # 几个QWidgets

        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        # 时间模块
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        # 图像模块
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        # 垂直布局

        layout = QVBoxLayout()
        layout.addWidget(self.startBtn)
        layout.addWidget(self.endBtn)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # 数组初始化
        self.x = []

    def showTime(self):
        shuju = np.random.random_sample() * 10  # 返回一个[0,1)之间的浮点型随机数*10
        self.x.append(shuju)  # 数组更新
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.clear()
        ax.plot(self.x)
        self.canvas.draw()

    # 启动函数
    def startTimer(self):
        # 设置计时间隔并启动
        self.timer.start(100)  # 每隔一秒执行一次绘图函数 showTime
        self.startBtn.setEnabled(False)  # 开始按钮变为禁用
        self.endBtn.setEnabled(True)  # 结束按钮变为可用

    def endTimer(self):
        self.timer.stop()  # 计时停止
        self.startBtn.setEnabled(True)  # 开始按钮变为可用
        self.endBtn.setEnabled(False)  # 结束按钮变为可用
        self.x = []  # 清空数组


# 运行程序
if __name__ == '__main__':
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    app.exec()
