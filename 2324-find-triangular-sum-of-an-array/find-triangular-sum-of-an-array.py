from math import comb
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            res+= comb(n-1,i)* nums[i]
        return res%10
