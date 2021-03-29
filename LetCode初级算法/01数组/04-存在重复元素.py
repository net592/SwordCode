"""
给定1个数组，将数组中的元素向右移动k个位置，其中k是非负数。
思路：简单的一种，用另外1个数组来记录旋转后的内容，然后复制回原数组，当然记录时是从nums.length-k个元素开始记录，记录到末尾后再去从头记录到刚才那个元素。
需要注意的是这里并非返回1个数组，程序会直接读取原数组位置的内容来检查，所以需要把旋转后的结果1个个复制回去。
还有，给出的k可能会大于数组长度，这时候就要对原数组取模，才会得到真正需要旋转的个数！（这是我没有考虑到的！）
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] == nums[i+1]:
                return True
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 比较重复数是否小于 总长度
        if len(set(nums)) < len(nums):
            return True
        else:
            return False