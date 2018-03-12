#-*- coding:utf-8 -*-
'''
多进程测试multiprocessing
'''
import multiprocessing
from time import ctime,sleep

def super_player(file,stime):
    '''
    创建多进程将要执行的函数
    :param file:播放文件的名称
    :param stime:延时
    :return:
    '''
    for i in range(2):
        print('Start playing %s! %s'%(file,ctime()))
        sleep(stime)

lists={'我和你':3 ,'天天向上':4,'大河之舞':5}

Threads=[]
files=range(len(lists))

for file,time in lists.items():
    t=multiprocessing.Process(target=super_player,args=(file,time))
    Threads.append(t)

if __name__=='__main__':
    for t in files:
        Threads[t].start()
    for t in files:
        Threads[t].join()