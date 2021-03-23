INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        
    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)
    
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()#去掉头尾的空白字符
        sign = 1
        #空字符串,不能转换,直接返回0
        if not s:
            return 0
        '''
        考虑几种情况：
        1.第1个非空字符是正号或负号
        2.第1个非空字符是数字
        (数字中间夹了其余非数字字符的话就不考虑后面的内容了)
        3.第1个非空字符不是正负号或数字,直接返回0
        '''
        if s[0] in ['+','-']:
            if s[0]=='-':
                sign = -1
            s = s[1:]
        res = 0
        for c in s:
            if c.isdigit():
                res = res*10+int(c)
            else:
                #代表数字中间夹了其余非数字字符的话就不考虑后面的内容了
                break
        res *= sign
        #判断溢出
        if res>2147483647:
            return 2147483647
        if res<-2147483648:
            return -2147483648
        return res