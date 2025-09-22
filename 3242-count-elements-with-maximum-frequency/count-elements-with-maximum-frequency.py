class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        maxi = 0
        c=0
        for i in nums:
            d[i] = 1 + d.get(i,0)
            maxi = max(maxi,d[i])
        for i in d:
            if d[i]==maxi:
                c+=1
        return c*maxi
