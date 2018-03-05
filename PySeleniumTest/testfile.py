#-*- coding:utf-8 -*-
import time
from datetime import datetime
from driverset.webDriverset import driver
dt=datetime.now()
print(dt.strftime('%H:%M:%S'))

driver.get('https://www.cnblogs.com/')
time.sleep(2)
#driver.find_element_by_id('//*[@id="span_userinfo"]/a[1]').click()
#time.sleep(1)
# allcookie=driver.get_cookies()
# for cookie in allcookie:
#     print('cookie=',cookie)
#     if cookie['name'] in ['.CNBlogsCookie','.Cnblogs.AspNetCore.Cookies']:
#         driver.add_cookie(cookie)
#         print(cookie)
#     time.sleep(1)

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

# cookie1=driver.get_cookie('Hm_lpvt_91e60d36b7b06785f72ce1797a6be307')
# cookie2=driver.get_cookie('Hm_lvt_91e60d36b7b06785f72ce1797a6be307')

# print(cookie2)
# print(cookie1)

# driver.add_cookie({'name':'HMACCOUNT','value':'C19CA88A508BDA58'})
# driver.add_cookie({'name':'Hm_lpvt_91e60d36b7b06785f72ce1797a6be307','value':'1520234068'})
# driver.add_cookie({'name':'Hm_lvt_91e60d36b7b06785f72ce1797a6be307','value':'1520234068'})
# driver.add_cookie({'name':'city','value':'145'})
# driver.add_cookie({'name':'remember_2c4dfcda1fe961d9c0edb7496454c865','value':'91294%7CgRKgJaYxJDnOssFzETk3q3d71sUq6o72C1gkl9dgfClZoHCwmg4MVjTxaTo1'})

time.sleep(4)
driver.refresh()
#driver.get('http://www.dongfangfuli.com/user/center?city=145')

#driver.delete_all_cookies()