#-*- coding:utf-8 -*-
'''
自动化测试-使用百度进行试验

'''
import time
from driverset.webDriverset import driver
from selenium .webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains  #导入鼠标操作事件
from selenium.webdriver.common.keys import Keys #模拟键盘事件
from selenium.webdriver.support.ui import WebDriverWait #等待方法
from selenium.webdriver.support import expected_conditions as EC #判断元素是否存在

driver.get('http://www.baidu.com')
#time.sleep(3)

#使用隐式等待方法，设置超时时间5S
driver.implicitly_wait(5)

#等待并判断网页是否加载完成
baidu=WebDriverWait(driver,5,0.5).until(EC.title_is('百度一下，你就知道'))
print('等待title加载',baidu)

cp=driver.find_element(By.ID,'jgwab').text
#cp=driver.find_element_by_id('jgwab').text
print(cp)
driver.find_element_by_class_name('s_ipt').send_keys('AutoTest')
elem=driver.find_element_by_id('su').get_attribute('value')
assert'百度一下'==elem
print('elem',elem)

#driver.find_element_by_id('kw').click()
driver.find_element_by_class_name('s_ipt').submit()  #除了点击按钮的方式，还可以针对表单使用submit

#使用is_displayed判断网页加载情况

for i in range(10):
    try:
        data=driver.find_element_by_id('kw')
        if data.is_displayed():
            break
    except:
        pass
    time.sleep(0.5)
else:
    print('timeout')

#driver.set_window_size(800,400) #设置浏览器大小
driver.back()
#time.sleep(2)

driver.forward()

driver.refresh()    #浏览器刷新

#time.sleep(2)
driver.find_element_by_id('kw').clear() #清除之前输入的文本

#鼠标悬停操作（设置）
elem2=driver.find_element_by_class_name('pf')
ActionChains(driver).move_to_element(elem2).perform()

#打开搜索设置
driver.find_element_by_link_text('搜索设置').click()
time.sleep(2)
print(driver.find_element_by_id('sugConf').text)
#保存搜索设置
driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
#获取提示框中的文本信息
print(driver.switch_to_alert().text)
#接收提示框信息
driver.switch_to_alert().accept()
#拒绝提示框信息
#driver.switch_to_alert().dismiss()

time.sleep(2)
#模拟键盘事件，将浏览器全屏显示
driver.find_element_by_class_name('pf').send_keys(Keys.F12)

driver.back()
time.sleep(3)
#以下为多窗口切换功能========
#获得当前窗口句柄
current_handle=driver.current_window_handle
#源窗口上的登录功能
login=driver.find_elements_by_link_text('登录')
login[0].click()    #有两个登录标签，选择第一个
#进入注册窗口
driver.find_element_by_link_text('立即注册').click()

#获取所有窗口的句柄
all_handle=driver.window_handles

#进入注册窗口，找到协议信息
for hanle in all_handle:
    if hanle!=current_handle:   #表示此句柄为注册窗口
        driver.switch_to.window(hanle)
        print(driver.find_element_by_id('TANGRAM__PSP_3__isAgreeWrapper').text)


#返回搜索窗口，进行搜索
for hanle in all_handle:
    if hanle==current_handle:
        driver.switch_to.window(hanle)
        #关闭登录窗口
        driver.find_element_by_id('TANGRAM__PSP_4__titleButtons').click()

        driver.find_element_by_id('kw').send_keys('黄山迎客松')

#清除搜索内容
#driver.find_element_by_id('kw').clear()

#操作滚动条
driver.set_window_size(600,600)
js='window.scrollTo(450,450)'  #左边距，上边距
driver.execute_script(js)

time.sleep(1)
driver.maximize_window()