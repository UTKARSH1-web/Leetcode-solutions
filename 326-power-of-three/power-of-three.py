import math 
class Solution:
    
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            a = math.log10(n) / math.log10(3)
            return a-int(a)==0
