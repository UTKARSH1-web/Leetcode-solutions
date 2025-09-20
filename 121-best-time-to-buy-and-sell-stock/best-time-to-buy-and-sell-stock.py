class Solution:
    def maxProfit(self,prices):
        maxi = 0
        profit=0
        m = prices[0]
        for i in range(1,len(prices)):
            cost = prices[i] - m
            profit = max(cost,0)
            maxi = max(profit,maxi)
            m = min(prices[i],m)
            # print(cost,profit,maxi,m)
        return maxi
        

