#-*- coding:utf-8 -*-
'''
Web自动化测试
处理登录的相关信息
'''
import time
from ITSWeb import path
from driverset.webDriverset import driver
from selenium.webdriver.common.keys import Keys

driver.get('http://10.243.140.117:9090/CY-Web//')
#driver.maximize_window()    #浏览器窗口最大化
driver.get_screenshot_as_file(path+'new.jpg')
#driver.implicitly_wait(10)
#断言title=百度一下，你就知道
assert u'金仕达新一代投资管理系统 v2.0 - 登录' in driver.title
assert u'金仕达新一代投资管理系统' in driver.page_source
assert u'欢迎使用金仕达软件' in driver.page_source
assert u'请登录系统管理后台' in driver.page_source

usercode= driver.find_element_by_xpath('//*[@id="reme"]').text
#print('usercode=%s'%usercode)
#assert driver.find_element_by_id('loginButton').text =='登录'

print(u'当前url:%s'%(driver.current_url))

elem=driver.find_element_by_name('UserCode')
#print('elem1',elem.text)
elem.send_keys('admin')

elem=driver.find_element_by_name('Password')
#print('elem2',elem.text)
elem.send_keys(u'kingstar',Keys.RETURN)  #Keys.RETURN模拟键盘的回车操作
print(u'当前url:%s'%(driver.current_url))

driver.get_screenshot_as_file(path+'login.jpg')
time.sleep(3)

#验证登录名正确
print('当前登录用户：',driver.find_element_by_class_name('username').text)
assert 'Admin'==driver.find_element_by_class_name('username').text
assert u'开户向导' in driver.page_source

#展开报表下拉菜单
elem=driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[6]/a/span[1]')
#print('elem3',elem.text)
elem.click()
print(u'当前url:%s'%(driver.current_url))