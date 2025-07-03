class Solution:
    def kthCharacter(self, k: int) -> str:
        s="a"
        while len(s)<k:
            a=""
            for i in s:
                a+= chr(ord(i)+1)
            s+=a
            # print(s)
        return s[k-1]