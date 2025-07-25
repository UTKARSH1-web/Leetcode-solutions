class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        else:
            return sum([x for x in set(nums) if x>0])