#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 21:03:48 2022

"""

from PyQt5.QtWidgets import QApplication, QWidget
import sys
app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(400, 100, 300, 200)
window.setWindowTitle('My first app')


window.show()
app.exec()