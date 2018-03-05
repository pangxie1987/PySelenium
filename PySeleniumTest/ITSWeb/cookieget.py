#-*- coding:utf-8 -*-
'''
通过添加cookie，绕过登录，直接打开登录后的url
必须先手工登录过一次，并且勾选‘下次自动登录’
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


#=====================百度个人中心，使用cookie绕过登录时验证码的验证==========
driver.get('http://www.baidu.com/')
driver.maximize_window()
time.sleep(2)
#login=driver.find_elements_by_link_text('登录')
#login[0].click()
#time.sleep(3)

#添加cookie，使用浏览器cookie查看获得
driver.add_cookie({'name':'BAIDUID','value':'687E54CDFDD9987424FA00471C8762A5:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'czfnlscGExeHJIQ2Jva0F5cmJEa1czdmZibVhSakpnSGdWZHhJd3lwdzVnOEJhQVFBQUFBJCQAAAAAAAAAAAEAAADmR5Eut9y2t9Ch86bQtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADn2mFo59phaaV'})
#添加后刷新浏览器句柄即可
driver.refresh()
time.sleep(2)
#登录成功后  获取登录名称
username=driver.find_element_by_class_name("user-name").text
print(username)


#=====================东方福利网，使用cookie绕过登录时验证码的验证==========
driver.get('http://www.dongfangfuli.com/?city=145')
time.sleep(2)
driver.add_cookie({'name':'HMACCOUNT','value':'C19CA88A508BDA58'})
driver.add_cookie({'name':'Hm_lpvt_91e60d36b7b06785f72ce1797a6be307','value':'1520234068'})
driver.add_cookie({'name':'Hm_lvt_91e60d36b7b06785f72ce1797a6be307','value':'1520234068'})
driver.add_cookie({'name':'city','value':'145'})
driver.add_cookie({'name':'remember_2c4dfcda1fe961d9c0edb7496454c865','value':'91294%7CgRKgJaYxJDnOssFzETk3q3d71sUq6o72C1gkl9dgfClZoHCwmg4MVjTxaTo1'})

time.sleep(3)
driver.refresh()

username=driver.find_element_by_xpath('/html/body/header/div[1]/div/div[1]/a[1]').text
print(username)

#=====================博客园，使用cookie绕过登录时验证码的验证==========
driver.get('https://www.cnblogs.com/')
time.sleep(2)

#cookie不能简单的使用name和value,要构造一个完整的cookie串，同时注意cookie的时效性（Expires）
cookie1={u'domain': u'.cnblogs.com',
            u'name': u'.CNBlogsCookie',
            u'value': u'A6835772FC5D59CFD5932272A40A1343BABC300E371C4E37B69D7EE8BC06F52E9AB089E6EFC936AC30984EE75CF11F681FF758594B515D64E63810720AE1AE874A083AA9B045A1BB369FF137BC419F560C718386',
            u'Expires': 1791887887,
            u'path': u'/',
            u'httpOnly': True,
            u'secure': False}

cookie2={u'domain': u'.cnblogs.com',
            u'name': u'.Cnblogs.AspNetCore.Cookies',
            u'value': u'CfDJ8Gf3jjv4cttDnEy2UYRcGZ04KqpchTjdddtvEwxmUXF0QgyT2PO-YNy4seTqR_2itf-qOuYcbqehUFyRNBxaKi6tZ_Cc65yLIJ0O9fREMrj77HWrNMEQt9KA6OBUyYV8xd40lyB9YuZbWOM2c6Nty9DOwWK_ZKnE59mw52qWaeoN3hQwPg3qBXauORv8tj3SK55hBsPBaFLcou9T6UzV7KR5IYBchXKg2_vHCHLoGIWs5lpN2mAsrOvArUMRY-yQpYUGxFCkFuNC6VXhTPi1BQVeTeZ_aXC-9jHkGDlHnRlZVSCvpprPsp-k3UwnfYVV6g',
            u'Expires': 1791887887,   #cookie超时时间
            u'path': u'/',
            u'httpOnly': True,
            u'secure': False}

driver.add_cookie(cookie1)
driver.add_cookie(cookie2)

time.sleep(4)
driver.refresh()

#获取登录后的用户名称
username=driver.find_element_by_id('span_userinfo').text
print(username)