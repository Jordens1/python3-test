#/usr/bin/env python
# _*_ coding:utf-8 _*_
import win32api
import win32con
#win32api.MessageBox(None,"Hello,pywin32!","pywin32",win32con.MB_OK)


import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        time.sleep(2)
        print(x,y)

except KeyboardInterrupt:
    print('\nExit.')


'''
87 456  平台管理
76 593
321 321
279 927
262 424
581 424  n-1次
281 442  （18） 332 460
（18）
282 460    (18)    337 478 
796 590
1399 276

'''

# import subprocess
# import win32api
# import time
# prs=subprocess.Popen([r'C:\Program Files (x86)\Google\Chrome\Application\chrome'])
# time.sleep(1)
# pree=pyautogui.hotkey('ctrl', 'shift', 'n')
#
# time.sleep(2)
# pyautogui.typewrite('http://geek.csdn.net/news/detail/86546', interval=0.25)
# pyautogui.press('enter')
# pyautogui.press('enter')
# time.sleep(2)
# win32api.TerminateProcess(int(prs._handle), -1)


