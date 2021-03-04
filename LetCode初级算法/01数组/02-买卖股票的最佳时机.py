"""
给定1个数组，它的第i个元素是1支给定股票第i天的价格。
设定1个算法来计算你所能获取的最大利润，你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
思路：我们遍历股价，遇到不断下降的趋势，我们就等降到了最低再买，然后等他开始上涨到最高点的时候卖出，以此往复，每次的收益累计就是最大收益了。
精华思路：只要第2天有上涨就买入卖出，做短线。
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        思路：只要第2天有上涨就买入卖出，做短线
        '''
        sum = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                sum += prices[i+1] - prices[i]
        return sum