#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:50:46 2022

@author: zhouguangdi
"""

import scipy as sp
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch 
from mpl_toolkits.mplot3d import proj3d
    
# 该类从https://stackoverflow.com/questions/11140163/python-matplotlib-plotting-a-3d-cube-a-sphere-and-a-vector/11156353#11156353 (last accessed: June 17, 2017)中获取
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args,\
                                 **kwargs) 
        self._verts3d = xs, ys, zs
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d,\
                                           renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

###字体设置###################################
font1 = {'weight': 'bold',
    'size': 26,
    'family': 'times new roman',
    }

font2 = {'weight': 'bold',
    'size': 24,
    'family': 'times new roman',
    }


#创建图形对象
fig = plt.figure() 
fig.set_size_inches(10.72, 8.20)  #画布大小

ax = fig.add_subplot(1,1,1,projection='3d')

#在 xy 平面上绘制波
x = np.linspace(0,2*sp.pi,50)
y = np.sin(x)
z = np.zeros(x.size)
#plt.hold(True)
ax.plot(x,-y*1.76,z,'k', lw = 2)
ax.plot(x,z,y,'k', lw = 2)

# 绘制矢量E和B
xv = np.linspace(0,2*sp.pi,16)
yv = np.sin(xv)
zv = np.zeros(xv.size) 
for i in range(len(xv)):
    a = Arrow3D([xv[i], xv[i]], [0 ,-yv[i]*1.76], [0,0],\
         mutation_scale = 10, lw=2, arrowstyle="-|>",\
                                 ls='dashed', color='b')
    ax.add_artist(a)
    b = Arrow3D([xv[i], xv[i]], [0,0], [0,yv[i]],\
         mutation_scale=10, lw=2, arrowstyle="-|>",\
                                 ls='dotted', color='r')
    ax.add_artist(b)

# 绘制矢量k
a = Arrow3D([-0.7,2.5*sp.pi], [0,0], [0,0], mutation_scale = 10, lw = 2, arrowstyle="-|>", color = 'k')
ax.add_artist(a)

#设置轴的属性
ax.set_xlim(0,7.5)
ax.set_ylim(-1.4,1.4)
ax.set_zlim(-1.2,1.2)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
plt.axis('off')

# 设置相机角度以获得良好的可视化效果
ax.elev=20
ax.azim=19


##图在画布上的占比、图片保存################################################################
plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)

# 标记向量
ax.text(2.5*np.pi, -0.2, -0.2,r'$\vec{k}$',**font1)
ax.text(np.pi/2, -2, 0, r'$\vec{B}$',**font1)
ax.text(np.pi/2, 0, 1.1, r'$\vec{E}$',**font1)

# 显示绘制
plt.show()

fig.savefig('./3_1用于演示光波横向性质的python代码.pdf')

















