# -*- coding:utf-8 -*-
'''
webdriver设置
'''
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
#chrome_options=options 去掉浏览器‘Chrome正收到自动测试软件的控制’的提示
driver=webdriver.Chrome(chrome_options=options,executable_path='C:\Python\chromedriver.exe')
driver.maximize_window()    #浏览器窗口最大化


