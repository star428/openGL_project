#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: circle.py
@time: 2020/11/4 23:13
@desc:
"""
from otherFuction import *


def Circle(position, windowSize):
    x = position[0]
    y = position[1]
    r = position[2]

    x0 = 0
    y0 = r

    p0 = 5 / 4 - r
    points = []

    addAllPoints(points, x0, y0, x, y, windowSize)

    while x0 < y0:
        if p0 < 0:
            x0 += 1
            p0 = p0 + 2 * x0 + 1
        else:
            x0 += 1
            y0 -= 1
            p0 = p0 + 2 * x0 + 1 - 2 * y0
        addAllPoints(points, x0, y0, x, y, windowSize)

    return points


def addAllPoints(points, x0, y0, x, y, windowSize):
    addPoints(points, x + x0, y + y0, windowSize)
    addPoints(points, x + x0, y - y0, windowSize)
    addPoints(points, x - x0, y + y0, windowSize)
    addPoints(points, x - x0, y - y0, windowSize)
    addPoints(points, x + y0, y + x0, windowSize)
    addPoints(points, x + y0, y - x0, windowSize)
    addPoints(points, x - y0, y + x0, windowSize)
    addPoints(points, x - y0, y - x0, windowSize)
