class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        new = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                new.append(nums[i])
            else:
                continue
        c=0
        for i in range(1,len(new)-1):
            if new[i]> new[i-1] and new[i]>new[i+1]:
                c+=1
            elif new[i]< new[i-1] and new[i]<new[i+1]:
                c+=1
        return c