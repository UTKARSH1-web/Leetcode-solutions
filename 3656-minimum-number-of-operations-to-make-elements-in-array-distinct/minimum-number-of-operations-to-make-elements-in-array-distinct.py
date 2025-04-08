class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=len(nums)
        s=set()
        id=-1
        for i in range(n-1,-1,-1):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                # print(i)
                id=i
                break
        if len(s)==len(nums):
            return 0
        else:
            return math.ceil((id+1)/3)
