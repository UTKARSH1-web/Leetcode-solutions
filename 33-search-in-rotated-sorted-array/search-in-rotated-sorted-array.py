class Solution:
    def findPivot(self,nums,n):
        l=0
        r = n-1
        while l<r:
            mid = l + (r-l)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r=mid
        return r
    def binary(self,l,r,nums,target):
        ind = -1
        while l<=r:
            mid = mid = l + (r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return ind
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = self.findPivot(nums,n)
        ind = self.binary(0,pivot-1,nums,target)
        if ind!=-1:
            return ind
        else:
            return self.binary(pivot,n-1,nums,target)
