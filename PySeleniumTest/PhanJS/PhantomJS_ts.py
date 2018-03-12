#-*- coding:utf-8 -*-
'''
PhantomJs测试，无界面启动，速度会更快
'''
from selenium import webdriver
import time

driver=webdriver.PhantomJS()
driver.get('http://www.baidu.com')
time.sleep(3)
driver.get_screenshot_as_file('baidu.jpg')

driver.find_element_by_id('kw').send_keys('PhantomJS')
driver.find_element_by_id('su').submit()
time.sleep(3)
driver.get_screenshot_as_file('PhantomJS.jpg')