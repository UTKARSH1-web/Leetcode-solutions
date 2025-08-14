class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        l = []
        c = []
        def comb(i,n,k,l,c):
            if len(c)==k:
                l.append(c[:])
                return 
            for j in range(i,n+1):
                # if j not in c:
                c.append(j)
                comb(j+1,n,k,l,c)
                c.pop(-1)
        i=1
        comb(i,n,k,l,c)
        return l

                