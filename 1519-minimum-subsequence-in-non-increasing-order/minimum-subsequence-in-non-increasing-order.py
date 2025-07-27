class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        ans=[]
        c=0
        s= sum(nums)
        i=0
        while sum(ans)<=s:
            ans.append(nums[0])
            s-=nums[0]
            nums.pop(0)
            
            
        return ans
