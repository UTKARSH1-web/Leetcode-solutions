class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        def dfs(node):
            vis[node]=True
            for i in adj[node]:
                if vis[i]==False:
                    dfs(i)
        n = len(mat)
        adj = [[] for _ in range(n)]
        c=0
        for i in range(n):
            for j in range(n):
                if mat[i][j]==1:
                    adj[i].append(j)
        vis = [False]*(n)
        for i in range(n):
            if not vis[i]:
                dfs(i)
                c+=1
        return c
        
            