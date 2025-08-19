class Solution:
    
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c=0
        z=0
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
            else:
                c+= (z*(z+1))//2
                z=0
        if z > 0:
            c += (z * (z + 1)) // 2

        return c