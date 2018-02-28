#-*- coding:utf-8 -*-
'''
unittest
使用博客园进行测试，因登录需要验证，代码失效
'''
import unittest
import time
from selenium import webdriver
from driverset.webDriverset import driver
#driver=webdriver.Chrome(executable_path='C:\Python\chromedriver.exe')

class loginCase(unittest.TestCase):
    def login(self,username,password):
        driver.get('https://passport.cnblogs.com/user/signin')
        driver.find_element_by_id('input1').send_keys(username)
        driver.find_element_by_id('input2').send_keys(password)
        driver.find_element_by_id('signin').click()  # 点击登陆按钮

    #@staticmethod
    def test_login_sucess(self):
        self.login('吃螃蟹','lpb1987#')
        time.sleep(1)
        assert driver.find_element_by_id('lnk_current_user').text
        link=driver.find_element_by_id('lnk_current_user').text
        self.assertTrue('吃螃蟹' in link)

if __name__=='__main__':
    testsuit=unittest.TestSuite()
    testsuit.addTest(loginCase('test_login_sucess'))