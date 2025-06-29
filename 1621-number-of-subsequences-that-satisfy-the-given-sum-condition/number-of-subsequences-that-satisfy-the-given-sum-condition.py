class Solution:
    def be(self,a, n, m):
        result = 1
        a = a % m
        while n > 0:
            if n % 2 == 1:
                result = (result * a) % m
            a = (a * a) % m
            n //= 2
        return result

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n= len(nums)
        MOD = 10**9 +7
        i=0
        j=n-1
        res = 0
        while i<=j :
            if (nums[i] + nums[j]) <= target:
                pw = self.be(2,j-i,MOD)
                res+=pw
                i+=1
            else:
                j-=1
        return res%MOD


