class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        cnt=0
        d[0]=1
        remove=0
        presum=0
        for i in nums:
            presum+=i
            remove = presum-k
            cnt+=d.get(remove,0)
            d[presum] = d.get(presum,0) +1
        return cnt