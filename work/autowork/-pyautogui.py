#/usr/bin/env python
# _*_ coding:utf-8 _*_
import pyautogui
import time

# 鼠标光标在屏幕左上角，PyAutoGUI函数就会产生pyautogui.FailSafeException异常
pyautogui.FAILSAFE = True
# 可以为所有的PyAutoGUI函数增加延迟
pyautogui.PAUSE = 0.4

x, y = pyautogui.center( (16, 448, 191, 21) )
pyautogui.click( x, y )
# pyautogui.click( x=87, y=456, button='left' )
x, y = pyautogui.center( (43, 585, 87, 15) )
pyautogui.click( x, y )
# pyautogui.click( x=76, y=593, button='left' )
for yeshu in range(12, 14):
    for num in range(1, 105):
        #回退的地方
        x, y = pyautogui.center( (256, 316, 107, 21) )  # 获得中心点
        pyautogui.click( x, y )
        # pyautogui.click(x=321, y=321, button='left')
        pyautogui.click(x=279, y=927, button='left')
        pyautogui.click(x=262, y=424, button='left')
        hangshu = 1
        while hangshu < yeshu:
            pyautogui.click(x=581, y=424, button='left')
            hangshu += 1
        #第35个开始就从最后开始
        if 69 > num > 34:
            num = num - 35
            #-576 刚好下一页    -1500 以上最后
            pyautogui.scroll(-576)
        elif num > 68:
            num = num - 69
            pyautogui.scroll(-1600)

        pyautogui.click(x=281, y=442 + (16 * num), button='left')
        # 默认
        pyautogui.click(x=332, y=460 + (16 * num), button='left')
        pyautogui.click(x=795, y=595, button='left')
        pyautogui.click(x=1399, y=276, button='left')
        #huitui --->
        pyautogui.alert('这个消息弹窗是文字+OK按钮')
        # pyautogui.locateOnScreen( 'huitui.png' )
        x, y = pyautogui.center( (1864, 215, 24, 16) )  # 获得中心点
        pyautogui.click( x, y )
    time.sleep(3)