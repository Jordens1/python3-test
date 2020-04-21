#/usr/bin/env python
# _*_ coding:utf-8 _*_

import pygame
import time

#音乐路径
path = r'C:\python3test\视在\autowork\xxx.mp4'
#初始化
pygame.mixer.init()
#加载音乐
track = pygame.mixer.music.load(path)
#播放音乐
pygame.mixer.music.play()
#暂停
time.sleep(10)
pygame.mixer.music.pause()

#停止
pygame.mixer.music.stop()















