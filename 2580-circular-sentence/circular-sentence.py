class Solution:
    def isCircularSentence(self, s: str) -> bool:
        l = list(map(str,s.split()))
        f=True
        for i in range(len(l)):
            if l[i-1][-1] != l[i][0]:
                f=False
        return f
        