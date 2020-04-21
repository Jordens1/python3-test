#/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
了解xml： https://www.w3schools.com/xml/   存储和传输数据，没有被预定义标签    html用来显示数据
XPath 在xml查找信息的语言   是路径表达式
常用路径表达式：
//  不考虑位置
./   当前节点
@   选取属性
*  所有元素节点

谷歌浏览器插件：xpath helper      快捷键  shift ctrl x
'''

'''
属性定位
//div[@class="SDkEP"]
//div[@class="pR49Ae gsfi"]
索引定位   索引从一开始
//div[@class="SDkEP"]/div[1]/div//span
逻辑运算
//div[@class="a4bIc" and @jsname="gLFyf"] 
模糊匹配
//input[contains(@class, "s")]

'''
import lxml










