class Solution:
    def NumberOf1(self, n):
        # write code here
        if n<0:
            n=n&0xffffffff
        return bin(n).count("1")

"""
左移解法

同样上面的例子我们设置一个flag = 1, temp = 0, count = 1,下面我们分析过程:
我们还是用 0000 0101 和 flag 进行与运算,但这次我们不必将负数进行补码的求解,开始 flag = 1, 与运算后 结果为1 ,则count += 1
,temp += 1, 下面我们将flag进行左移,得到 10,再将其与0000 0101 进行与运算,得到 0, temp += 1,
......继续一直这样运算下去,直到temp = 32(数字有32位),结束.代码如下:
"""
class Solution:
    def NumberOf1(self, n):
        # write code here
        # flag 与 N进行 位左移计算
        step = 0
        flag = 1
        count = 0
        while step < 32:
            if flag & n: # flag与n做位运算 1就是匹配
                count += 1
            flag = flag << 1
            step +=1
        return count