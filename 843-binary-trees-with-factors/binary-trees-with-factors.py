class Solution:
    def numFactoredBinaryTrees(self, a: List[int]) -> int:
        a.sort()
        d={}
        for i in a:
            d[i] =(sum(d[b] * d.get(i/b, 0 ) for b in d if i %b==0) + 1) % (10**9 +7)
        return sum( d.values())% (10**9 +7)
