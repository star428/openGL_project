#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: Breseham_Line.py
@time: 2020/11/4 21:42
@desc:
"""
from otherFuction import *


# 简单实例请填充其余情况
def BresehamLine(position, windowSize):
    # x, y = changeCoordinate(position, windowSize)
    # qp.drawPoint(x, y)
    if position[0] > position[2]:
        position = (position[2], position[3], position[0], position[1])
    points = []
    # 初始端点为左端点
    x = position[0]
    y = position[1]

    dx = abs(int(position[2] - position[0]))
    dy = abs(int(position[3] - position[1]))
    if dx >= dy:
        p = 2 * dy - dx
        twoDy = 2 * dy
        twoDyMinusDx = 2 * (dy - dx)

        addPoints(points, x, y, windowSize)

        while x < position[2]:
            x += 1
            if p < 0:
                p += twoDy
            else:
                y += 1
                p += twoDyMinusDx

            addPoints(points, x, y, windowSize)
    else:
        p = 2 * dx - dy
        twoDx = 2 * dx
        twoDzMinusDy = 2 * (dx - dy)
        addPoints(points, x, y, windowSize)

        while y < abs(position[3]):
            y += 1
            if p < 0:
                p += twoDx
            else:
                x += 1
                p += twoDzMinusDy

            addPoints(points, x, y, windowSize)

    if (position[3] - position[1]) < 0:
        newPoints = []
        for index in range(len(points)):
            point = refreshCoordinate(points[index], windowSize)
            # 复原原来的point值
            point = (point[0], 2 * position[1] - point[1])
            addPoints(newPoints, point[0], point[1], windowSize)

        points = newPoints

    return points
