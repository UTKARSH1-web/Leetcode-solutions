class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        a= set()
        i=0
        ans=0
        j=0
        n= len(nums)
        while j<n:
            if nums[j] not in a:
                a.add(nums[j])
                ans=max(ans,sum(a))
                j+=1
            else:
                a.remove(nums[i])
                i+=1
        return ans
