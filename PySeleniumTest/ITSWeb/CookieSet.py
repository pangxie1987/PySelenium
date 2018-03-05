#-*- coding:utf-8 -*-
'''
获取cookie并打印出来
'''
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

'''
设置cookie,绕过登录
'''
#name   JSESSIONID
#value 6114216E74B17A382D6BEDE7727B8E62