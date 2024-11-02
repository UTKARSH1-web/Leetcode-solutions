class Solution:
    def isCircularSentence(self, s: str) -> bool:
        return all(s.split()[i-1][-1] == s.split()[i][0] for i in range(len(s.split())))


        
        