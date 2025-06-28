class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        sorted_k = sorted(sorted_nums[-k:],key = lambda x:x[0])
        # print(sorted_k)
        return [i for x,i in sorted_k]
