#-*- coding:utf-8 -*-
'''
多线程分布式执行测试案例
'''
from selenium import webdriver
from time import ctime,sleep
import threading
from driverset.serverstart import check_exsit

def test_baidu(host,browser):
    '''
    构造测试用例
    :param host:
    :param browser:
    :return:
    '''
    print('Start Test')
    print(host,browser)
    # dc={'browsername',browser}
    # driver=webdriver.Remote(command_executor=host,
    #                         desired_capabilities=dc)

    driver = webdriver.Remote(  # executable_path='C:\Python\chromedriver.exe',
        command_executor=host,
        desired_capabilities={'platform': 'ANY',
                              'browserName': browser,  # 浏览器
                              'version': '',
                              'javascriptEnabled': True,
                              }
    )
    sleep(3)
    driver.get('http://www.baidu.com')

    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').submit()

if __name__=='__main__':
    #启动参数（指定运行主机与浏览器）
    lists = {'http://127.0.0.1:5556/wd/hub': 'chrome',
             'http://127.0.0.1:5555/wd/hub': 'firefox'}

    threads=[]
    files=range(len(lists))

    for host,browser in lists.items():
        t=threading.Thread(target=test_baidu,args=(host,browser))
        threads.append(t)

    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
