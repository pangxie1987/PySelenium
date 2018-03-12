#-*- coding:utf-8 -*-
'''
selenium+Remote参数化平台及浏览器
首先要启动
'''
import time
import os
from  selenium.webdriver import Remote
from driverset.serverstart import check_exsit


#设计主机+浏览器运行模式
lists={'http://127.0.0.1:5556/wd/hub':'chrome',
       'http://127.0.0.1:5555/wd/hub':'firefox'}

for host,brwoser in lists.items():
    print(host,brwoser)
    driver=Remote(#executable_path='C:\Python\chromedriver.exe',
              command_executor=host,
              desired_capabilities={'platform':'ANY',
                                    'browserName':brwoser, #浏览器
                                    'version':'',
                                    'javascriptEnabled':True,
                                    }
                )

    driver.get('http://wwww.baidu.com')
    driver.find_element_by_id('kw').send_keys('remote')
    driver.find_element_by_id('su').click()
