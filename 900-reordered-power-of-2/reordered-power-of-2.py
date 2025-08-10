class Solution:
    def isTwo(self, n: str) -> bool:
        L  =["011237","0122579","012356789","0124","0134449", "0145678","01466788","0248","0368888","0469","1","112234778","11266777","122446","125","128","1289","13468","16","2","224588","23","23334455","234455668","23678","256","35566","4","46","8"]
        return n in L

    # def recurPermute(self,ds, nums, ans, freq):
    #         if len(ds) == len(nums):
    #             if ds not in ans:   
    #                 ans.append(ds[:])
    #             return
    #         for i in range(len(nums)):
    #             if not freq[i]:
    #                 ds.append(nums[i])
    #                 freq[i] = 1
    #                 self.recurPermute(ds, nums, ans, freq)
    #                 freq[i] = 0
    #                 ds.pop()

    # def convert(self,nums):
    #     l= []
    #     for i in nums:
    #         c=''
    #         for j in i:
    #             c+=str(j)
    #         l.append(c)
    #     return l

    def reorderedPowerOf2(self, n: int) -> bool:
        
        ans = ''.join(sorted(str(n)))
        return  self.isTwo(ans)
