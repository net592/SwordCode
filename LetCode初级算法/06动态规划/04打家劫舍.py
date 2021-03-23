class Solution:
    def rob(self, nums: List[int]) -> int:
        # 使用标准DP思路解题，时间和空间复杂度是O(n)
        # 处理特殊
        if len(nums) ==0:
            return 0
        # 2间房子取最大
        elif len(nums) <= 2:
            return max(nums)

        # 初始化状态DP  0 , 1
        dp = [nums[0], max(nums[0], nums[1])]

        for n in range(2, len(nums)):
            # 2.递推公式 根据算法子序列，f(n) = max(f(n-2) + 第n间屋子金额，f(n-1))
            # 3.状态缓存
            # 计算追加每次动态规划值
            dp.append( max(dp[n-1], dp[n-2] + nums[n]) )
        return max(dp)