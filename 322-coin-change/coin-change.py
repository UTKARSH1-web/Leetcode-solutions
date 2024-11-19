class Solution:
    def coinChange(self, coins: List[int], n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for j in coins:
                if i-j >=0:
                    dp[i] = min(dp[i],dp[i-j] +1)
        return dp[n] if dp[n]!=float('inf') else -1
