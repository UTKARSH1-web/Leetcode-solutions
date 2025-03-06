class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d={}
        for i in grid:
            for j in i:
                d[j] = 1 + d.get(j,0)
        for i in d:
            if d[i]==2:
                rep = i
        n = len(grid)*len(grid[0])
        miss  = (n*(n+1))//2 - sum(d.keys())
        return [rep,miss]