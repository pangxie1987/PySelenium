#-*- coding:utf-8 -*-
from driverset.webDriverset import driver
import ITSWeb.login

#获取cookie
cookies=driver.get_cookies()
print(cookies)
cookie_name=cookies[0]['value']
print('cookie_name:',cookie_name)

for cookie in cookies:
    print(cookie['name'],cookie['value'])
    #driver.delete_all_cookies() #删除cookies
    #print(driver.get_cookies())