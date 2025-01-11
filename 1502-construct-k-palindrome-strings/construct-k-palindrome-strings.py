class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) <k:
            return False
        d={}
        for i in s:
            d[i] = 1 + d.get(i,0)
        c=0
        for i in d:
            if d[i]%2!=0 :
                c+=1
        return c<=k
        