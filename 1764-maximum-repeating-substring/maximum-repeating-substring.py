class Solution:
    def maxRepeating(self, s: str, word: str) -> int:
        c=0 
        a= word
        while s.find(a)!=-1:
            c+=1
            a = a + word
        return c