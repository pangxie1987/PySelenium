# -*- coding:utf-8 -*-
'''
python+selenium进行web自动化测试
处理交易报表
'''
import time
import ITSWeb.login
from driverset.webDriverset import driver
from ITSWeb import path
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#打开交易报表
elem=driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[6]/ul/li[1]/a')
elem.click()
print(u'当前url:%s'%(driver.current_url))
driver.get_screenshot_as_file(path+'trade.jpg')
#收起菜单(否则打印按钮找不到)
elem=driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[1]/div[1]')
elem.click()

#需要进行iframe切换（界面采用了frame嵌套的方式）
#driver.switch_to_frame(0)
driver.switch_to.frame(0)   #根据iframe的index，0表示第一个
time.sleep(1)

# #切换句柄
# all_handles=driver.window_handles
# print(all_handles)
# current_handle=driver.current_window_handle
# driver.switch_to_window(all_handles[1])

#定位到时间匡
elem=driver.find_element_by_xpath('//*[@id="dateRange"]/i')
print(elem.text)
elem.click()

#选择上个月
elem=driver.find_element_by_xpath('/html/body/div[12]/div[3]/ul/li[6]')
elem.click()

#点击查询按钮
elem=driver.find_element_by_xpath('//*[@id="commonSearch"]/i')
elem.click()
driver.get_screenshot_as_file(path)

#打印按钮
elem=driver.find_element_by_xpath('//*[@id="frmfutureEntrustGridState"]/a[3]')
#elem.click()

#driver.quit()
