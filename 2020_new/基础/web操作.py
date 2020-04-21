#/usr/bin/env python
# _*_ coding:utf-8 _*_

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()     # 创建Chrome对象.
# 操作这个对象.
driver.get('http://33.93.201.86:8006')     # get方式访问百度.
time.sleep(2)
driver.save_screenshot("baidu.png")
# id="kw"是百度搜索框，输入字符串“微博”，跳转到搜索中国页面
driver.find_element_by_id("kw").send_keys(u"微博")
# id="su"是百度搜索按钮，click() 是模拟点击
driver.find_element_by_id("su").click()
# 获取新的页面快照
# time.sleep(2)

driver.save_screenshot(u"微博.png")
# 打印网页渲染后的源代码
# 获取当前页面Cookie
# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# 输入框重新输入内容
driver.find_element_by_id("kw").send_keys("test")
# 模拟Enter回车键
# time.sleep(2)

driver.find_element_by_id("su").send_keys(Keys.RETURN)
# 清除输入框内容
driver.find_element_by_id("kw").clear()
# 生成新的页面快照
driver.save_screenshot("test.png")
# 获取当前url
# time.sleep(2)


driver.quit()









