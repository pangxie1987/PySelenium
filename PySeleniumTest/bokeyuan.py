#-*- coding:utf-8 -*-
'''
unittest HTMLTestRunner
使用博客园进行测试，因登录需要验证，代码失效
'''
import unittest
import time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class loginCase(unittest.TestCase):
    '''博客园测试'''
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='C:\Python\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.base_url='https://www.cnblogs.com/'
        self.driver.get(self.base_url)


        cookie1 = {u'domain': u'.cnblogs.com',
                   u'name': u'.CNBlogsCookie',
                   u'value': u'A6835772FC5D59CFD5932272A40A1343BABC300E371C4E37B69D7EE8BC06F52E9AB089E6EFC936AC30984EE75CF11F681FF758594B515D64E63810720AE1AE874A083AA9B045A1BB369FF137BC419F560C718386',
                   u'Expires': 1791887887,
                   u'path': u'/',
                   u'httpOnly': True,
                   u'secure': False}

        cookie2 = {u'domain': u'.cnblogs.com',
                   u'name': u'.Cnblogs.AspNetCore.Cookies',
                   u'value': u'CfDJ8Gf3jjv4cttDnEy2UYRcGZ04KqpchTjdddtvEwxmUXF0QgyT2PO-YNy4seTqR_2itf-qOuYcbqehUFyRNBxaKi6tZ_Cc65yLIJ0O9fREMrj77HWrNMEQt9KA6OBUyYV8xd40lyB9YuZbWOM2c6Nty9DOwWK_ZKnE59mw52qWaeoN3hQwPg3qBXauORv8tj3SK55hBsPBaFLcou9T6UzV7KR5IYBchXKg2_vHCHLoGIWs5lpN2mAsrOvArUMRY-yQpYUGxFCkFuNC6VXhTPi1BQVeTeZ_aXC-9jHkGDlHnRlZVSCvpprPsp-k3UwnfYVV6g',
                   u'Expires': 1791887887,  # cookie超时时间
                   u'path': u'/',
                   u'httpOnly': True,
                   u'secure': False}

        self.driver.add_cookie(cookie1)
        self.driver.add_cookie(cookie2)
        time.sleep(3)
        self.driver.refresh()

    def test_username(self):
        '''验证登录后的用户名'''
        driver=self.driver
        username=driver.find_element_by_id('span_userinfo').text
        print(username)
        #assert username=='吃螃蟹'

    #@staticmethod
    def test_login_sucess(self):
        '''验证登录成功'''
        driver = self.driver
        current_urt=driver.current_url
        print(current_urt)
        # assert driver.find_element_by_id('lnk_current_user').text
        # link=driver.find_element_by_id('lnk_current_user').text
        # self.assertTrue('吃螃蟹' in link)

    def tearDown(self):
        self.driver.quit()

# def suitcase():
#     testsuit = unittest.TestSuite()
#     testsuit.addTest(loginCase('test_login_sucess'))
#     testsuit.addTest(loginCase('test_username'))
#     return testsuit

def main():
    print('Case start')
    name = time.strftime('%Y-%m-%d %H_%M_%S')
    print('name', name)

    with open(name + 'result.html', 'wb') as fp:
        print('创建测试报告成功')
        runner = HTMLTestRunner(stream=fp, title='博客园测试报告', description='测试用例执行结果')
        testsuit = unittest.TestSuite()
        testsuit.addTest(loginCase('test_login_sucess'))
        testsuit.addTest(loginCase('test_username'))
        runner.run(testsuit)
        fp.close()
        # unittest.main()


if __name__=='__main__':
    print('unit test start')
    main()