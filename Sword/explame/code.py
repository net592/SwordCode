# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if 0 <= number <=2:
            return number
        # 处理数据
        fOne = 1
        fTwo = 2
        for i in range(3,number + 1):
            fN = fOne + fTwo
            fOne = fTwo
            fTwo = fN
        return fN