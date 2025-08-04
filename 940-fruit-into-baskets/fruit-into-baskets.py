class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        a= {}
        i=0
        ans=0
        j=0
        n = len(nums)
        while j<n:
            if nums[j] not in a and len(a)<2:
                a[nums[j]]=a.get(nums[j],0) +1
                ans = max(ans,j-i+1)
                j+=1
            elif nums[j] in a :
                ans = max(ans,j-i+1)
                a[nums[j]]+=1
                j+=1
            else:
                a[nums[i]]-=1
                if a[nums[i]]==0:
                    del a[nums[i]]
                i+=1
        return ans