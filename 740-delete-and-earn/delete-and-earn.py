class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        house = [0] * (max_num + 1)
        
        for num in nums:
            house[num] += num
        n=len(house)
        if n<2:
            return max(house)
        dp=[0]*(n)
        dp[0]=house[0]
        dp[1]=house[1]
        
        for i in range(2,n):
            dp[i] = max(dp[i-2]+house[i],dp[i-1])
        # print(dp)
        return max(dp)