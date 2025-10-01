class Solution:
    def numWaterBottles(self, bottles: int, exchange: int) -> int:
        c=0
        n=bottles
        c=n
        while n>=exchange:
            r=n%exchange
            q=n//exchange
            n=r+q
            c+=q
            # print(r,q,c,n)
        return c


