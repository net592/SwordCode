"""
Q:大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n≤39
注释：斐波那契数列（Fibonacci sequence） 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
在数学上，斐波那契数列以如下被以递推的方法定义：F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*

"""

# -*- coding:utf-8 -*-
class Solution:
    """
    方法一：递归
    优点，代码简单好写，缺点：慢，会超时, 不能使用
    时间复杂度：O(2^n)
    空间复杂度：递归栈的空间
    """
    def Fibonacci(self, n):
        # write code here
        if n <= 39:
            if n == 0 or n == 1:
                return n
            else:
                return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)


class Solution:
    def __init__(self):
        self.tmp_dict = {}
    def Fib(self, n):
        if n <= 39:
            if n == 0 or n == 1:
                return n
            else:
                self.tmp_dict[n] = self.tmp_dict[n - 1] + self.tmp_dict[n - 2]
                return self.Fib(n - 1) + self.Fib(n - 2)

class Solution:
    """
    方法二：叠加
    优点，代码简单好写，缺点：慢，会超时
    时间复杂度：O(2^n)
    空间复杂度：递归栈的空间
    """
    def Fibonacci(self, n):
        # write code here
        # write code here
        res=[0,1,1,2]
        while len(res)<=n:
            res.append(res[-1]+res[-2])
        print(res)
        return res[n]

# -*- coding:utf-8 -*-
class Solution:
    """
    递归，为了提高效率，我们需要利用一个辅助的结果列表result，计算过的n和Fibonacci(n)对储存在里面，避免重复计算
    """"
    def Fibonacci(self, n):
         # write code here
         result = {0:0, 1:1}
         def helper(n):
             if n in result:
                 return result[n]
             res = helper(n-1) + helper(n-2)
             result[n] = res
             return res
         return helper(n)



if __name__ == '__main__':
    s=Solution()
    print(s.Fibonacci(39))