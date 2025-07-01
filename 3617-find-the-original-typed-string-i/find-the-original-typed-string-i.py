class Solution:
    def possibleStringCount(self, word: str) -> int:
        c=0
        x=0
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                x+=1
            else:
                c+=x
                x=0
        c+=x
        return c+1
