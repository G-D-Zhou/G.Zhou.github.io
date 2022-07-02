#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:42:51 2022

"""

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # GUI 属性
        self.setGeometry(400, 100, 300, 200)
        self.setWindowTitle('My first app')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    app.exec_()
