class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp_max = 0 # 临时最大数
        res = nums[0] # 假设法第一个数最大
        for num in nums:
            tmp_max = max(num, tmp_max +num) # 最大tmp_max
            res = max(tmp_max, res) # 最大max
        return res