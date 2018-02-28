# -*- coding:utf-8 -*-
'''
webdriver设置
'''
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path='C:\Python\chromedriver.exe')
driver.maximize_window()    #浏览器窗口最大化

