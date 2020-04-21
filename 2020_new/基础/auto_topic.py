#/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys, os, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main(url, username, password, device_id):
    driver = webdriver.Chrome()     # 创建Chrome对象.
    driver.implicitly_wait( 20 )        # 隐形等待时间，最长时间
    wait = WebDriverWait(driver, 10)     # 显性等待时间
    try :
        # 操作这个对象.
        driver.get( url )  # get方式访问
        driver.save_screenshot("login.png")
        wait.until( EC.title_is('登录'))
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_xpath('//button').click()        # 点击登录
        wait.until( EC.title_is('主页') )
        driver.save_screenshot("loginin.png")
        driver.find_element_by_xpath('//ul[@id="side-menu"]/li[5]//span[@class="nav-label"]').click()      # 平台管理
        shuchulink = driver.find_element_by_xpath('//div[@class="sidebar-collapse"]//li[5]/ul/li[11]/a')     # 输出资源管理
        url = shuchulink.get_attribute( 'href' )        # 提取a标签内的链接，注意这里提取出来的链接是字符串
        driver.get( url )       # 不能用click，因为click点击字符串没用，直接用浏览器打开网址即可
        wait.until(EC.presence_of_element_located((By.ID, 'add-Topic')))
        driver.find_element_by_xpath('//button[@onclick="ResouceMager.TopicMager()"]').click()        # topic管理
        wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="添加Topic"]')))
        for id1 in device_id:
            output_source(driver, id1, wait)
        driver.back()
        wait.until( EC.title_is('主页') )
        driver.find_element_by_xpath('//ul[@id="side-menu"]/li[5]//span[@class="nav-label"]').click()      # 平台管理
        shuchupei = driver.find_element_by_xpath( '//div[@class="sidebar-collapse"]//li[5]/ul/li[12]/a' )  # 输出配置
        pei_url = shuchupei.get_attribute( 'href' )
        for id2 in device_id:
            driver.get( pei_url )
            wait.until( EC.presence_of_element_located( (By.XPATH, '//button[text()="批量解绑"]') ) )
            output_config(driver, id2, wait)
    finally:
        driver.quit()


def output_source(driver, id, wait):
    topic_id = "tq_" + id
    time.sleep(1)
    add_topic = driver.find_element_by_xpath('//button[@onclick="ResouceMager.addTopic()"]')       # 添加topic
    add_topic.click()
    wait.until( EC.presence_of_element_located( (By.XPATH, '//label[text()="TopicName"]') ) )
    driver.find_element_by_xpath('//div[@class="col-sm-9"]//input[@name="topicName"]').send_keys(topic_id)       # 添加topic_id
    driver.find_element_by_xpath('//div[@class="form-group text-center"]/button[1]').click()        # 保存
    time.sleep(num)


def output_config(driver, id, wait):
    driver.find_element_by_xpath('//input[@placeholder="搜索"]').send_keys(id)       # 筛选点位
    time.sleep(1)
    # wait.until( EC.invisibility_of_element_located(( By.XPATH, '//tr[@data-index="1"]' )))
    driver.find_element_by_xpath('//i[@class="fa fa-edit"]').click()        # 编辑
    wait.until(EC.presence_of_element_located((By.XPATH, "//option")))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='ibox float-e-margins']/div[2]/div/ul/li")))
    topic_id = 'tq_' + id
    # 选取下拉框的值
    s1 = Select(driver.find_element_by_xpath('//select[@name="srsids"]'))        # 实例化Select
    s1.select_by_visible_text(topic_id)
    time.sleep(num)
    # wait.until( EC.element_to_be_selected(( By.XPATH, "//option" )) )
    driver.find_element_by_xpath('//button[contains(text(),"添加topic")]').click()        # 添加topic
    time.sleep(num)
    # a = driver.find_element_by_xpath('//a[3]')
    # driver.execute_script( "arguments[0].click();", a )


def get_id(device_file):
    device_id = []
    with open(device_file, 'r') as f:
        for line in f.readlines():
            device_id.append(line.strip())
    return device_id


if __name__ == '__main__':
    num = 0.2
    url = r'http://33.93.201.86:8006'
    username = 'admin'
    password = 'admin'
    device_file = os.getcwd() + '\\' + sys.argv[1]
    device_id = get_id(device_file)
    main(url, username, password, device_id)

