#-*- coding:utf-8 -*-
'''
通过添加cookie，绕过登录，直接打开登录后的url
必须先手工登录过一次
'''
from driverset.webDriverset import driver
import time
import logging

logging.basicConfig(level=logging.DEBUG)    #设置日志级别
#============测试ITSWeb通过cookie绕过登录===========
# driver.get('http://10.243.140.117:9090/CY-Web/')
# driver.delete_all_cookies()
# time.sleep(6)
# driver.add_cookie({'name': 'JSESSIONID', 'secure': False, 'httpOnly': True, 'path': '/CY-Web/', 'domain': '10.243.140.117', 'value': '8A36623788D2FCF28EEEBD49EDA846B4'})
# #driver.add_cookie({'value':'6114216E74B17A382D6BEDE7727B8E62'})
# time.sleep(1)
# print(driver.get_cookies())
# driver.refresh()
# driver.get('http://10.243.140.117:9090/CY-Web/manager/home.do')
#
# time.sleep(5)
# assert u'开户向导' in driver.page_source
# print('Sucess!')


#=====================使用cookie绕过登录时验证码的验证==========
driver.get('http://www.baidu.com/')
driver.maximize_window()
time.sleep(2)
login=driver.find_elements_by_link_text('登录')
login[0].click()
time.sleep(3)
#driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()

# cookies=driver.get_cookies()
# for cookie in cookies:
#     driver.add_cookie(cookie)
#     print(cookie)

#添加cookie，使用浏览器cookie查看获得
driver.add_cookie({'name':'BAIDUID','value':'687E54CDFDD9987424FA00471C8762A5:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'czfnlscGExeHJIQ2Jva0F5cmJEa1czdmZibVhSakpnSGdWZHhJd3lwdzVnOEJhQVFBQUFBJCQAAAAAAAAAAAEAAADmR5Eut9y2t9Ch86bQtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADn2mFo59phaaV'})
#添加后刷新浏览器句柄即可
driver.refresh()
time.sleep(5)
#登录成功后  获取登录名称
username=driver.find_element_by_class_name("user-name").text
print(username)
