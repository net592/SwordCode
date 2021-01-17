"""
Python3 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
思路：
栈A用来作入队列
栈B用来出队列，当栈B为空时，栈A全部出栈到栈B,栈B再出栈（即出队列）
在Python环境下，原生的list即为一个栈实现，我们直接通过定义两个list即可定义出两个栈：
1、首先要明确队列的特性是先进先出，栈的特性是先进后出；
2、A进队列的方法里我们只要有容器能装元素就行了，所以直接往栈1里压；
3、在出队列方法B里，要保证出队列的是最先进入的元素：
4、在往栈2压完一批元素后，栈1进了新的元素想往栈2压的时候，栈2必须把上一批的元素清空了才行(也就是栈2必须是空的)。
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = [] # 入栈
        self.stack2 = [] # 出栈
    def push(self, node):
        # write code here
        self.stack1.append(node) # 入值
    def pop(self):
        # return xx
        if self.stack2 == []: # 将入栈存入B栈
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

