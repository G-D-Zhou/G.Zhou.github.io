#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Point:
    """
    该类用于表示笛卡尔坐标系中的点。
    """

    def __init__(self, x, y):
        """
        创建坐标为(x, y)的点
        """
        self.x = x
        self.y = y
    
    def translate(self, dx, dy):
        """
        在 x 和 y 方向将点平移 dx 和 dy。
        """
        self.x += dx
        self.y += dy
    
    def __str__(self):
        return("Point at [%f, %f]"%(self.x, self.y))
    
