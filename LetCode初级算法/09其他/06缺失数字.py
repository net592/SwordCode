"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。


"""

class Solution:
    def missingNumber(self, nums):
        # 用set 比较num +1 来判断结果
        num = set(nums)
        
        # +1加上缺失数
        n = len(num) + 1
        
        for i in range(n):
            if i not in nums:
                return i