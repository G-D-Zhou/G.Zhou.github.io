#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:53:48 2022

@author: zhouguangdi
"""

# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # GUI 属性
        self.setGeometry(480, 120, 360, 240)
        self.setWindowTitle('My first app')
        # 标签
        ## 标签1: 纯文本
        label1 = QLabel('My first application says: ', self)
        label1.setFixedWidth(160)   # 设定标签的宽度
        label1.move(10, 10)
        ## 标签2: 富文本
        label2 = QLabel("", self)
        message = "<h3><b><font color='green'>Hello Python!</font></b>" 
        # 试着更改HTML的标签看会发生什么
        label2.setText(message)
        label2.setFixedWidth(120)
        label2.move(165,10)
        ## 标签3: 图像
        label3 = QLabel("", self)
        label3.setPixmap(QPixmap("greating.svg")) 
        #可在当前目录中使用图像替换greating.svg
        label3.setFixedSize(50,50)
        label3.show()
        label3.move(280,10)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    app.exec_()