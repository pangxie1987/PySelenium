#-*- coding:utf-8 -*-
import os
import time
import win32com.client


def check_exsit(process_name):
    '''
    判断selenium server是否启动，如果没有，则启动
    :param process_name:
    :return:
    '''
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:
        print('%s is exists' % process_name)
    else:
        print('%s is not exists' % process_name)
        print('selenium server is starting now!')

        os.system('C:\Python\startup_selenium_server.bat')
        time.sleep(5)


check_exsit('java.exe')