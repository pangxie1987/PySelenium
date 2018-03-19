#-*- coding:utf-8 -*-
'''
从文件中读取整行，并将数据进行分离
'''
with open('userinfo','r') as f:
    user_info=f.readlines()
    print(user_info)
    for line in user_info:
        #print(line)
        username=line.split(',')[0]
        passwd=line.split(',')[1]
        print(username,passwd)