class Solution:
    def trap(self, h: List[int]) -> int:
        n=len(h)
        l=[0]*n
        r=[0]*n
        maxl=h[0]
        maxr=h[-1]
        t=0
        for i in range(1,len(h)):
            l[i]=maxl
            maxl=max(h[i],l[i])
        for i in range(len(h)-2,0,-1):
            r[i]=maxr
            maxr=max(h[i],r[i])
        for i in range(1,n-1):
            if h[i]<l[i] and h[i]<r[i]:
                t+=min(l[i],r[i])-h[i]
        return t
