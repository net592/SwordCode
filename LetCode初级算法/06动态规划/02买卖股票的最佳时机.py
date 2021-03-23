class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 使用动态规划方法求解
        minPrice = float("inf") # 构建最小值上限
        res = 0 # 初始利润值
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i]) # 求最小值
            res = max(res, prices[i] - minPrice) # 求最大差值
        return res