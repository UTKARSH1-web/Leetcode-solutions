class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        m=-1
        for i in arr:
            d[i] = 1 + d.get(i,0)
        for i in d:
            if d[i]==i:
                m=max(m,i)
        return m