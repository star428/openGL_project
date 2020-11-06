#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: otherFuction.py
@time: 2020/10/28 21:17
@desc:
"""


def changeCoordinate(position, windowSize):
    return (position[0] + windowSize.width() / 2,
            windowSize.height() / 2 - position[1])

def refreshCoordinate(position, windowSize):
    return (position[0] - windowSize.width() / 2,
            windowSize.height() / 2 - position[1])

def round(num):
    return int(num + 0.5)


def addPoints(points, x, y, windowSize):
    out_x, out_y = round(x), round(y)
    out_x, out_y = changeCoordinate((out_x, out_y), windowSize)
    points.append((out_x, out_y))
