"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
我们先来观察一下
跳到台阶1的方案：
① 0⇒1
跳到台阶2的方案：
① 0⇒1⇒2
② 0⇒2
跳到台阶3的方案：
① 0⇒1⇒2⇒3
② 0⇒2⇒3
③ 0⇒1⇒3
跳到台阶4的方案：
① 0⇒1⇒2⇒3⇒4
② 0⇒2⇒3⇒4
③ 0⇒1⇒3⇒4
④ 0⇒1⇒2⇒4
⑤ 0⇒2⇒4
可以发现：
跳到台阶4的方案是从台阶3跳1级或从台阶2跳2级
设：𝐹(𝑛) 表示跳到台阶 𝑛 (n＞2) 的方案数，
则 𝐹(𝑛)=𝐹(𝑛−1)+𝐹(𝑛−2)
"""
class Solution:
    """
    我们把n级台阶时的跳法看成n的函数，记为f(n)。
当n>=2时，第一次跳的时候有两种不同的选择：

第一次跳1级，此时跳法的数目等于后面剩下的n-1级台阶的跳法数目，即为f(n-1);
第一次跳2级，此时跳法数目等于后面剩下的n-2级台阶的跳法数目，即为f(n-2)。
因此，n级台阶的不同跳法总数为f(n) = f(n-1) + f(n-2)
    """
    def jumpFloor(self, number):
        # write code here
        #此题与菲波那切数列的本质一致
        if number == 1:
            return 1
        if number == 2:
            return 2
        fOne = 1
        fTwo = 2
        for i in range(3,number+1):
            fN = fTwo + fOne
            fOne = fTwo
            fTwo = fN
        return fN

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if 0<number<3:
            return number
        a,b=2,1
        for i in range(0,number-2):
            a,b=a+b,a
        return a