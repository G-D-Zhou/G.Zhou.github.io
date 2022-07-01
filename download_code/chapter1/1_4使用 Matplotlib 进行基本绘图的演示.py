#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt     # 导入库

x = [1, 3, 5, 6, 8, 10, 15]         # 定义x
y = x                               # 定义y

plt.figure()                        # 创建一个新图
plt.plot(x, y)                      # 绘制 f(x) = x
plt.xlabel("X-Axis")                   # 标注x轴
plt.ylabel("Y-Axis")                   # 标注y轴
plt.show()                          # 仅当调用 plt.show() 时才会显示绘图结果
