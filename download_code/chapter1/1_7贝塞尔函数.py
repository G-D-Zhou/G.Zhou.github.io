#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:58:09 2022

"""

from scipy.special import jn, yn, jn_zeros, yn_zeros
import matplotlib.pyplot as plt
import numpy as np

n = 0       # 阶数
x = 0.0

# 第一类贝塞尔函数
print("J_%d(%f) = %f" % (n, x, jn(n, x)))

x = 1.0
# 第二类贝塞尔函数
print("Y_%d(%f) = %f" % (n, x, yn(n, x)))

# 贝塞尔函数的零点
n = 0        # 阶数
m = 4        # 要计算的根数
print("贝塞尔函数的零点是：", jn_zeros(n, m))

# 绘制贝塞尔函数
x = np.linspace(0, 10, 50)
markers = ['o', 's', '*', '+']
lines = ['-', '--', '-.', ':']

fig, ax = plt.subplots()
for n in range(4):
    ax.plot(x, jn(n, x), ls = str(lines[n]), 
                    marker = str(markers[n]), label = r"$J_%d(x)$" % n)
ax.legend()
plt.show()