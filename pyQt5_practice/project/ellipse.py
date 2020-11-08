#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: ellipse.py
@time: 2020/11/4 23:25
@desc:
"""
from otherFuction import *


def Ellipse(position, windowSize):
    xc = position[0]
    yc = position[1]
    rx = position[2]
    ry = position[3]
    points = []  # (x, y)形式的对作为points里面的每一项

    rx2 = rx ** 2
    ry2 = ry ** 2
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2

    x = 0
    y = ry
    px = 0
    py = two_rx2 * y

    # region 1
    p = round(ry2 - (rx2 * ry) + (0.25 * rx2))
    while (px < py):
        x += 1
        px += two_ry2
        if p < 0:
            p += ry2 + px
        else:
            y -= 1
            py -= two_rx2
            p += ry2 + px - py

        addPoints(points, xc + x, yc + y, windowSize)
        addPoints(points, xc - x, yc + y, windowSize)
        addPoints(points, xc + x, yc - y, windowSize)
        addPoints(points, xc - x, yc - y, windowSize)
        """
        addPoints(points,  +x,  +y, windowSize)
        addPoints(points,  -x,  -y, windowSize)
        addPoints(points,  +x,  -y, windowSize)
        addPoints(points,  -x,  +y, windowSize)
        """
    # region 2
    p = round(ry2 * (x + 0.5) ** 2 + rx2 * (y - 1) ** 2 - rx2 * ry2)
    while y > 0:
        y -= 1
        py -= two_rx2
        if p > 0:
            p += rx2 - py
        else:
            x += 1
            px += two_ry2
            p += rx2 - py + px

        addPoints(points, xc + x, yc + y, windowSize)
        addPoints(points, xc - x, yc + y, windowSize)
        addPoints(points, xc + x, yc - y, windowSize)
        addPoints(points, xc - x, yc - y, windowSize)
        """
        addPoints(points,  +x,  +y, windowSize)
        addPoints(points,  -x,  -y, windowSize)
        addPoints(points,  +x,  -y, windowSize)
        addPoints(points,  -x,  +y, windowSize)
        """
    return points
