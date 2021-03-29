import time
from functools import lru_cache
import collections


@lru_cache()        # 测试无缓存时将本行注释掉
def fib_memoization(number: int) -> int:
    if number == 0: return 0
    if number == 1: return 1

    return fib_memoization(number-1) + fib_memoization(number-2)


@lru_cache(maxsize=2)
def add(num):
    return num

class LRUCache(collections.OrderedDict):
    """
       function:利用collection.OrderedDict数据类型实现最近最少使用算法
                OrderedDict有个特殊方法popitem(Last=False)时则实现队列，弹出最先插入的元素，
                而当Last=True则实现堆栈方法，弹出的是最近插入的那个元素
                实现了两个方法：get(key）取出键中对应的值，若没有返回None
                                set(key, value) 根据LRU特性添加元素
        time: 2016年5月4日
    """
    def __init__(self, size=5):
        self.size = size
        self.cache = collections.OrderedDict()
     
    def get(self,key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            value = None
            return value
    def set(self,key, value):
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif self.size == len(self.cache):
            self.cache.popitem(last = False)
            self.cache[key] = value
        else:
            self.cache[key] = value

#基于普通dict和list实现
class LRUCache():
     def __init__( self , size=5 ):
         self.size = size
         self.cache = dict()
         self.key = []
 
     def get( self , key):
         if key in self.cache:
             self.key.remove(key)
             self.key.insert( 0 ,key)
             return self.cache[key]
         else :
             return None
 
     def set ( self , key, value):
         if key in self.cache:
             self.cache.pop(key)
             self.cache[key] = value
             self.key.remove(key)
             self.key.insert( 0 ,key)
         elif len ( self.cache) == self.size:
             old_key = self.key.pop()
             self.cache.pop(old_key)
             self.key.insert( 0 ,key)
             self.cache[key] = value
         else :
             self.cache[key] = value
             self.key.insert( 0 ,key)
             
if __name__ == '__main__':
    test = LRUCache(size=6)
    test.set('a',1)
    test.set('b',2)
    test.set('c',3)
    test.set('d',4)
    test.set('e',5)
    # 开关测试
    # test.set('f',6)
    print(test.get('a'))