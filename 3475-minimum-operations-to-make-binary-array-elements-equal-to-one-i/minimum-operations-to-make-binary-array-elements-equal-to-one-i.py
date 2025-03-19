class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i= 0
        j = 2
        n = len(nums)
        c=0
        while j<n:
            if nums[i]==0:
                for x in range(i,j+1):
                    nums[x] =1- nums[x]
                c+=1
            # print(nums)
            
            i+=1
            j+=1
        if sum(nums)==len(nums):
            return c
        else:
            return -1
