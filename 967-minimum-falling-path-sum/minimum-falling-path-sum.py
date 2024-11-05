class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        for i in range(1,n):
            for j in range(n):
                if j==0:
                    mat[i][j]=min(mat[i-1][j],mat[i-1][j+1]) + mat[i][j]
                elif j==n-1:
                    mat[i][j]=min(mat[i-1][j], mat[i-1][j-1])+mat[i][j]
                else:
                    mat[i][j] = min(mat[i-1][j-1],mat[i-1][j],mat[i-1][j+1])+mat[i][j]
        return min(mat[-1])