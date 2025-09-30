from math import comb
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        return sum(comb(len(nums) - 1, i) * nums[i] for i in range(len(nums))) % 10
