class Solution:
    def f(self,spell,potions,success):
        i = 0
        n =len(potions)
        j = len(potions)
        ans=0
        while i<j:
            mid = i + (j-i)//2
            if potions[mid]*spell >=success:
                ans = max(n - mid, ans)
                j = mid
            else:
                i=mid+1
        return ans

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        ans = [0]*n
        potions.sort()
        for i in range(n):
            ans[i] = self.f(spells[i],potions,success)
        return ans