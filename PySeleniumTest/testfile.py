#-*- coding:utf-8 -*-
import time
from datetime import datetime
from selenium import webdriver
from driverset.webDriverset import driver
dt=datetime.now()
print(dt.strftime('%H:%M:%S'))

from selenium.webdriver import Remote
lists={'http:127.0.0.1/wd/hub':'chrome'}
print(lists.items())
for host,browser in lists.items():

    print(host,browser)

br=webdriver.Firefox()
br.get('http://www.baidu.com')
br.find_element_by_id('kw').send_keys('上海金科路')
br.find_element_by_id('su').submit()