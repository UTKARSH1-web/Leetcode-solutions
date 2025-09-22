class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q=deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    newrow = row+dr
                    newcol = col+dc
                    if newrow in range(n) and newcol in range(m) and grid[newrow][newcol]=="1" and (newrow,newcol) not in visit:
                        q.append((newrow,newcol))
                        visit.add((newrow,newcol))
        n = len(grid)
        m = len(grid[0])
        visit= set()
        cnt=0
        for r in range(n):
            for c in range(m):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    cnt+=1
        return cnt