#-*- coding:utf-8 -*-
from datetime import datetime
dt=datetime.now()
print(dt.strftime('%H:%M:%S'))

try:
    print(aa)
except BaseException as msg:
    print(msg)
