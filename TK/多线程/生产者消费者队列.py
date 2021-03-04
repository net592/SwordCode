#!/usr/bin/env python
# set coding: utf-8
__author__ = "richardzgt"


import  threading,time
import queue


q = queue.Queue(maxsize=10)


def Producer():
    count = 1
    while True:
        q.put("g%s" % count)
        print("produer queue g%s" %count)
        count += 1
        time.sleep(1)

def Consumer():
    while True:
        good = q.get()
        print("Consumer queue ",good)
        time.sleep(5)



p = threading.Thread(target=Producer)
c = threading.Thread(target=Consumer)

p.start()
c.start()