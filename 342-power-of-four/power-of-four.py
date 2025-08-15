import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            a=math.log(n,4)
            if a- int(a)==0:
                return True
            return False