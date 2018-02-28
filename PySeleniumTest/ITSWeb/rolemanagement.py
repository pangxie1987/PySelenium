#-*- coding:utf-8 -*-
'''
Web自动化测试
处理角色管理
'''
from driverset.webDriverset import driver
import ITSWeb.login
import time
#打开运行维护
driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[4]/a/span[1]').click()

print('当前操作的url=%s'%(driver.current_url))
#打开角色管理
driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[4]/ul/li[1]/a').click()

driver.switch_to.frame(0)   #根据iframe的index，0表示第一个
time.sleep(3)
assert u'角色用户' in driver.page_source

# #新增
# driver.find_element_by_xpath('//*[@id="frmGridState"]/a[1]').click()
# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/a[2]').click()
#向上滚动到页面底部
driver.execute_script("window.scrollBy(document.body.scrollHeight,0)","")

#将菜单收起
#driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[1]/div[1]')

#定位到角色功能点
driver.find_element_by_xpath('//*[@id="tabstrip"]/ul/li[2]/span[2]').click()
time.sleep(6)
assert u'基本信息' in driver.page_source

#基本信息
ins=driver.find_element_by_class_name('k-in')
ins.click()
print('ins=%s'%(ins.text))

#查找所有的标签名称
tabnames=driver.find_elements_by_class_name('k-in')
for tabname in tabnames:
    print(tabname.text)

#基本信息复选框
message01=driver.find_element_by_class_name('k-checkbox-wrapper')
message01.click()

#找到所有的复选框
checkboxs=driver.find_elements_by_class_name('k-checkbox-wrapper')
# aaa=checkboxs.pop()
# aaa.click()
print('checkbox=',len(checkboxs))

checkboxss=driver.find_elements_by_tag_name('input')
time.sleep(3)
i=0
for checc in checkboxs:
    #if checc.get_attribute('type')=='checkbox':
        time.sleep(0.1)
        checc.click()
        i+=1
print('i=%s',i)

# che=driver.find_element_by_xpath('//*[@id="roleFunctionTree_tv_active"]/div/span[2]/label')
# che.click()
# #进行复选框选中的操作
# checkbox0=checkboxs.pop(0)
# checkbox0.click()