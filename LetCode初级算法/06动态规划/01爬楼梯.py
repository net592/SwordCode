class Solution:
    def climbStairs(self, n: int) -> int:
        # 特殊条件处理 n>0
        if n <= 2:
            return n
        # 构建初始值长度
        dp = [0]*n
		# 特殊值初始 台阶1 dp[0]=1 台阶2 dp[1]=2
        dp[0] =1 
        dp[1] =2
        for i in range(2,n): # 循环2, n-1个
            dp[i]=dp[i-1] + dp[i-2] # Fib
        return dp[n-1] # 返回N-1 因为起始台阶索引0