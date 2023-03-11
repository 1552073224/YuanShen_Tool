import cv2 as cv
import numpy as np
from PIL import Image
from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication
import win32gui
import sys
import time

hwnd_title = dict() #创建字典保存窗口的句柄与名称映射关系
def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t!= "":
        print(h, t)
i = 'Genshin Tools – main.py'
hwnd = win32gui.FindWindow(None, i)
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save(f"Images/{i}.jpg")

