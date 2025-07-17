class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        presum =0
        cnt =0
        for i in range(len(nums)):
            presum+=nums[i]
            remove = presum -k
            cnt +=d.get(remove,0)
            d[presum] = d.get(presum,0)+1
        return cnt