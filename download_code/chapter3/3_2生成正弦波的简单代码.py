#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入——标准模块
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt  
 
# 标准EM参数
wave_length = 555E-3 #波长为555 nm
initial_phase = np.pi/2 #初始相位为90度
wave_amplitute = 1 #波的振幅为1

#计算波
z = np.linspace(0,1,256)   #单位为um
k = 2*np.pi/wave_length    #波矢
psi = wave_amplitute*np.sin(k*z+initial_phase)   #波

#创建matplotlib图像
fig, ax = plt.subplots(1,1)
plt.plot(z,psi)
plt.show()
