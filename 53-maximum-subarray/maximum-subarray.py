class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi =-10**9
        curr = 0
        for i in range(len(nums)):
            curr+=nums[i]
            maxi = max(curr,maxi)
            if curr<0:
                curr=0
        return maxi