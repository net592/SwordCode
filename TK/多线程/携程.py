#!/usr/bin/env python
# -*- coding:utf-8 -*-
from greenlet import greenlet
def test1():
    print (11)
    gr2.switch()    #手动切换
    print (22)
    gr2.switch()

def test2():
    print (33)
    gr1.switch()
    print (44)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()