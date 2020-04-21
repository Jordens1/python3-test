#/usr/bin/env python
# _*_ coding:utf-8 _*_
import win32api, win32con, time


#设置鼠标的位置  x、y 坐标
win32api.SetCursorPos([30, 40])
time.sleep(0.1)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0)









