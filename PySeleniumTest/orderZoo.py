# -*- coding:utf-8 -*-
'''
上海野生动物园订票
'''
import time
from datetime import datetime
from selenium import webdriver

photopath='photo'
dt = datetime.now()
strtime = dt.strftime('%H%M%S')

driver = webdriver.Chrome(executable_path='C:\Python\chromedriver.exe')

driver.get('http://www.shwzoo.com/')
driver.maximize_window()
atdata1 = driver.find_element_by_css_selector('body > div.footer > div.wrap_1200 > p:nth-child(1)').text
print(atdata1)
assert atdata1 == '地址：上海市浦东新区南六公路178号'
atdata2 = driver.find_element_by_css_selector('body > div.footer > div.wrap_1200 > p:nth-child(2)').text
print(atdata2)
assert atdata2 == '电话：021-58036000'

driver.save_screenshot(photopath+'\\'+'%s'%strtime+'.jpg')

# driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li[8]/a').click()
# driver.find_element_by_xpath('/html/body/div[2]/div/p/a[1]').click()
# driver.find_element_by_name('txtUserName').send_keys('773779347@qq.com')

# driver.find_element_by_name('txtPassword').send_keys('lpb1987')
# driver.find_element_by_id('btnSubmit').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li[8]/a').click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/li[1]/a/div[1]/img').click()
# time.sleep(3)
# driver.find_element_by_class_name('add').click()
# driver.find_element_by_id('addtime').click()
# driver.find_element_by_xpath('//*[@id="laydate_table"]/tbody/tr[5]/td[4]').click()
#
# elem1=driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div[2]/ul[1]/li[2]/a').text
# print('elem1=',elem1)
# driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div[2]/ul[1]/li[2]/a').click()
#
# elem2=driver.find_element_by_class_name('layui-layer-content').text
# print('elem2',elem2)
# #购买提示弹窗，点击确定
# driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()
# time.sleep(2)
# #取票人资料
# elem4=driver.find_element_by_xpath('//*[@id="orderForm"]/div[1]/h6').text
#
#
# #验证取票人资料信息
# elem3=driver.find_element_by_xpath('//*[@id="orderForm"]/div[1]/dl[1]/dt').text
# print('elem3',elem3)
# assert u'联系人' in elem3
#
# #driver.close()