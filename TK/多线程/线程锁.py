#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time


num = 100 #设置一个共享变量

def lock_problem():
    #不加锁，线程抢占修改
    def show():
        global num  #在函数内操作函数外变量，需设置为全局变量
        time.sleep(1)
        num -= 1
    list=[]
    for i in range(100):
        t = threading.Thread(target=show)
        t.start()
        list.append(t)

    for t in list:
        t.join()
    print(num)
    time.sleep(1)

def lock():
    lock=threading.Lock()  #生成全局锁
    def show():
        global num  #在函数内操作函数外变量，需设置为全局变量
        time.sleep(1)
        lock.acquire()  #修改前加锁
        num -= 1
        lock.release()  #修改后解锁
    list=[]
    for i in range(100):
        t = threading.Thread(target=show)
        t.start()
        list.append(t)

    for t in list:
        t.join()

    print(num)
if __name__ == '__main__':
    lock_problem()
    num = 100
    lock()
    