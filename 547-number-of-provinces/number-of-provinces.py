class Solution:
    def findCircleNum(self, road: List[List[int]]) -> int:
        def dfs(node):
            vis[node] = 1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i)

        n = len(road)
        adj = [[] for _ in range(n)]
        vis = [0]*n
        for i in range(n):
            for j in range(n):
                if road[i][j] ==1:
                    adj[i].append(j)
        c=0
        for i in range(n):
            if vis[i]==0:
                c+=1
                dfs(i)
        
        return c

