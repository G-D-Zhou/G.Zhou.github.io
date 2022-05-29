#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 16:05:04 2022
"""

import matplotlib.pyplot as plt     
fig1 = plt.figure(1)                # 第一个figure
ax1 = plt.subplot(211)              # 第一个figure中的第一个子图
ax1.plot([1, 2, 3])
ax2 = plt.subplot(212)              # 第一个figure中的第二个子图
ax2.plot([4, 5, 6])                         
fig2 = plt.figure(2)                # 第二个figure
plt.plot([4, 5, 6])                 # 通过默认的方式创建子图(111)
fig1 = plt.figure(1)                # figure 1是当前的，子图(212)仍然是当前的
ax1 = plt.subplot(211)              # 使得子图(211)在figure 1 中成为当前的
ax1.set_title('Easy as 1, 2, 3')    # 子图(211)的题目
plt.show()