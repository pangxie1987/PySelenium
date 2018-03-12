#-*- coding:utf-8 -*-
'''
多线程的用法
'''

from time import sleep,ctime
import threading
import multiprocessing
#
# #=========多线程的优化==========
# #创建方法，将多线程的任务方法化
# def super_player(name,stime):
#     for i in range(2):
#         print('Start playing :%s!%s '%(name,ctime()))
#         sleep(stime)
#
# lists={'爱情买卖':2,'老男孩':4,'我和你':4}
#
# lens=range(len(lists))
#
# Threads=[]
# for file,time  in lists.items():
#     t=threading.Thread(target=super_player,args=(file,time))
#     Threads.append(t)
#
# if __name__=='__main__':
#     for t in lens:
#         Threads[t].start()
#     for t in lens:
#         Threads[t].join()

#===========继承所线程类threading==============
class Mythread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name

    #重写run函数
    def run(self):
        print('is runing now')
        self.func(*self.args)

def super_player(name,stime):
    for i in range(2):
        print('Start playing :%s!%s '%(name,ctime()))
        sleep(stime)

lists={'爱情买卖':2,'老男孩':4,'我和你':4}

lens=range(len(lists))

Threads=[]
for file,time  in lists.items():
    t=Mythread(super_player,(file,time),super_player.__name__)
    Threads.append(t)

if __name__=='__main__':
    for t in lens:
        Threads[t].start()
    for t in lens:
        Threads[t].join()

    print('All is ended')