#-*- coding:utf-8 -*-
import time
import sys
sys.path.append('C:\Python\Python34\Lib\site-packages')
sys.path.append('C:\WorkDay\Code\Python\PySeleniumTest')
from datetime import datetime
from selenium import webdriver
#from driverset.webDriverset import driver
import readtext
import Email

dt=datetime.now()
print(dt.strftime('%H:%M:%S'))
print('hello jenkins')
