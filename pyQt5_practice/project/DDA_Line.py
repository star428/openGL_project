#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: DDA_Line.py
@time: 2020/10/28 21:18
@desc:
"""
from otherFuction import *


def DDALine(position, windowSize):
    # x, y = changeCoordinate(position, windowSize)
    # qp.drawPoint(x, y)
    if position[0] > position[2]:
        position = (position[2], position[3], position[0], position[1])
    points = []
    dx = int(position[2] - position[0])
    dy = int(position[3] - position[1])

    x = position[0]
    y = position[1]

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    x_increase = float(dx) / float(steps)
    y_increase = float(dy) / float(steps)

    addPoints(points, x, y, windowSize)
    for step in range(steps):
        x += x_increase
        y += y_increase

        addPoints(points, x, y, windowSize)
    return points
