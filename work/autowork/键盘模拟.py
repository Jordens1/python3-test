#/usr/bin/env python
# _*_ coding:utf-8 _*_

import win32api, win32con, time

'''
#点击windows图标
win32api.keybd_event(91, 0, 0, 0)
time.sleep(0.1)
win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)

键盘键值表 当前目录下

还可以使用pyautogui
'''

#切换界面
while True:
    win32api.keybd_event(18, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(9, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(3)




