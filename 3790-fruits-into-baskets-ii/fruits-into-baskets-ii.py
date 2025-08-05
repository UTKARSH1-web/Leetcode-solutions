class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        rem = []
        for i in fruits[:]:
            for j in baskets:
                if j>=i:
                    baskets.remove(j)
                    fruits.remove(i)
                    break
                else:
                    continue
        
        return len(fruits)