class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n>1: # n小于等于1 退出
            if n % 3 != 0: # 取余计算 不等于0 无法整除
                return False
            # 递除3 
            n = n // 3
        return n == 1