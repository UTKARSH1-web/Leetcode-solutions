class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={}
        vowel =0
        const = 0
        for i in s:
            d[i] = 1 + d.get(i,0)
            if i in "aeiou":
                vowel = max(vowel,d[i])
            else:
                const = max(const,d[i])
        return vowel + const
