#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入 —— 标准模块
import sys

# 导入matplotlib，并设置其可以使用Qt5Agg来绘图
import matplotlib as mpl
mpl.use("Qt5Agg")

# 从PyQt5中导入：QtCore QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# 导入numpy模块
import numpy as np

# 导入matplotlib的后端
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from matplotlib.figure import Figure

# 从 matplotlib导入pyplot从而实现图像的绘制
from matplotlib import pyplot as plt

# 创建一个源自于FigureCanvas类的类。这是绘制正弦波的画布。
class MplCanvas(FC):
    def __init__(self,parent=None,width=8,height=6.5,lamda=555,\
                phi=np.pi/4,ampl=1):
        fig=Figure(figsize=(width,height))
        self.ax = fig.add_subplot(111)

        # 将绘图设置到画布上
        FC.__init__(self,fig)

        # 制定一些标准的图形策略
        FC.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FC.updateGeometry(self)
        
        self.drawPlot(lamda,phi,ampl)      #绘图

    def drawPlot(self,lamda,phi,ampl):
        z = np.linspace(0,0.7,1024)
        k = 2*np.pi/(lamda/1000)       #波矢
        psi = ampl*np.sin(k*z+phi)
        self.ax.cla()
        self.ax.plot(z,psi,'r')
        self.ax.set_ylim(-2,2)
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.draw()

#定义主窗口类        
class MainApp(QMainWindow):
    def __init__ (self):
        """构造函数或初始化程序"""
        QMainWindow.__init__(self)

        # 设置窗口的一些默认属性
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Wave")

        # 将主部件定义为 self
        self.main_widget = QWidget(self)

        # 添加标签部件和滑块
        # 波长
        self.loLambda = QVBoxLayout()
        self.lblLambda = QLabel("Wavelength (nm)", self)
        self.sldLambda = QSlider(Qt.Horizontal)
        self.sldLambda.setMinimum(400)
        self.sldLambda.setMaximum(700)
        self.sldLambda.setValue(700)
        self.sldLambda.setTickPosition(QSlider.TicksBelow)
        self.sldLambda.setTickInterval(5)
        self.edtLambda = QLineEdit(self)
        self.edtLambda.setMaxLength(5)
        self.loLambda.addWidget(self.lblLambda)
        self.loLambda.addSpacing(3)
        self.loLambda.addWidget(self.sldLambda)
        self.loLambda.addSpacing(3)
        self.loLambda.addWidget(self.edtLambda)
        
        # 初始相位
        self.loPhase = QVBoxLayout()
        self.lblPhase = QLabel("Initial Phase (rad)", self)
        self.sldPhase = QSlider(Qt.Horizontal)
        self.sldPhase.setMinimum(0)
        self.sldPhase.setMaximum(2*np.pi*100)
        self.sldPhase.setValue(0)
        self.sldPhase.setTickPosition(QSlider.TicksBelow)
        self.sldPhase.setTickInterval(1)
        self.edtPhase = QLineEdit(self)
        self.edtPhase.setMaxLength(5)
        self.loPhase.addWidget(self.lblPhase)
        self.loPhase.addSpacing(3)
        self.loPhase.addWidget(self.sldPhase)
        self.loPhase.addSpacing(3)
        self.loPhase.addWidget(self.edtPhase)            

        # 振幅
        self.loAmpl = QVBoxLayout()
        self.lblAmpl = QLabel("Amplitude", self)
        self.sldAmpl = QSlider(Qt.Horizontal)
        self.sldAmpl.setMinimum(10)
        self.sldAmpl.setMaximum(200)
        self.sldAmpl.setValue(100)
        self.sldAmpl.setTickPosition(QSlider.TicksBelow)
        self.sldAmpl.setTickInterval(1)
        self.edtAmpl = QLineEdit(self)
        self.edtAmpl.setMaxLength(5)
        self.loAmpl.addWidget(self.lblAmpl)
        self.loAmpl.addSpacing(3)
        self.loAmpl.addWidget(self.sldAmpl)
        self.loAmpl.addSpacing(3)
        self.loAmpl.addWidget(self.edtAmpl)

        # Waves Param Layout
        self.loWaveParams = QHBoxLayout()
        self.loWaveParams.addLayout(self.loLambda)
        self.loWaveParams.addStretch()
        self.loWaveParams.addLayout(self.loPhase)
        self.loWaveParams.addStretch()
        self.loWaveParams.addLayout(self.loAmpl)

        # 从滑块中获取值
        lamda = self.sldLambda.value()
        phi = self.sldPhase.value()/100
        ampl = self.sldAmpl.value()/100
        self.edtLambda.setText(str(lamda))
        self.edtPhase.setText(str(phi))
        self.edtAmpl.setText(str(ampl))

        # 创建一个FigureCanvas实例
        self.loCanvas = MplCanvas(self.main_widget,width=5,height=4,\
                                          lamda=lamda,phi=phi,ampl=ampl)

        # 将焦点设置到 main_widget 并将其设置为中心部件
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        # 填充主布局
        self.loMaster = QVBoxLayout(self.main_widget)
        self.loMaster.addLayout(self.loWaveParams)
        self.loMaster.addWidget(self.loCanvas)

        # 连接插槽
        self.sldLambda.valueChanged.connect(self.OnLambdaChanged)
        self.sldPhase.valueChanged.connect(self.OnPhaseChanged)
        self.sldAmpl.valueChanged.connect(self.OnAmplChanged)
        self.edtLambda.editingFinished.connect(self.OnEdtLambdaChanged)
        self.edtPhase.editingFinished.connect(self.OnEdtPhaseChanged)
        self.edtAmpl.editingFinished.connect(self.OnEdtAmplChanged)

    def OnLambdaChanged(self):
        lamda = self.sldLambda.value()
        self.edtLambda.setText(str(lamda))
        self.OnSomethingChanged()

    def OnPhaseChanged(self):
        phi = self.sldPhase.value()/100
        self.edtPhase.setText(str(phi))
        self.OnSomethingChanged()

    def OnAmplChanged(self):
        ampl = self.sldAmpl.value()/100
        self.edtAmpl.setText(str(ampl))
        self.OnSomethingChanged()

    def OnEdtLambdaChanged(self):
        lamda = int(self.edtLambda.text())
        self.sldLambda.setValue(lamda)

    def OnEdtPhaseChanged(self):
        phi = self.edtPhase.text()
        self.sldPhase.setValue(float(phi)*100)
        
    def OnEdtAmplChanged(self):
        ampl = self.edtAmpl.text()
        self.sldAmpl.setValue(float(ampl)*100)

    def OnSomethingChanged(self):
        lamda = self.sldLambda.value()
        phi = self.sldPhase.value()/100
        ampl = self.sldAmpl.value()/100
        self.loCanvas.drawPlot(lamda,phi,ampl)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApp = MainApp()
    MyApp.show()
    app.exec()

