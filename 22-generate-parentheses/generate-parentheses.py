class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        leftc = 0
        rightc = 0
        ans = []
        ds = []
        def rec(leftc,rightc,ans,ds,n):
            # print(ds)
            if leftc==n and rightc==n:
                ans.append(''.join(ds[:]))
                return
            if leftc< n :
                ds.append('(')
                rec(leftc+1,rightc,ans,ds,n)
                ds.pop()
            if rightc < n  and rightc<leftc:
                ds.append(')')
                rec(leftc,rightc+1,ans,ds,n)
                ds.pop()
        rec(leftc,rightc,ans,ds,n)
        return ans
                
