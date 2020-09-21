#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@contact: yewang863@gmail.com
@software: garner
@file: DDA_func.py
@time: 2020/9/21 下午9:48
@desc:
"""


def round(num):
    return int(num + 0.5)


def setPixel(x, y):
    """set the x , y"""
    pass


def lineDDA(x0, y0, xEnd, yEnd):
    dx = abs(x0 - xEnd)
    dy = abs(y0 - yEnd)
    x = x0
    y = y0
    steps = None
    if dx > dy:
        steps = dx
    else:
        steps = dy
    x_increase = dx / steps
    y_increase = dy / steps
    setPixel(round(x), round(y))
    for step in range(steps):
        x += x_increase
        y += y_increase
        setPixel(round(x), round(y))
