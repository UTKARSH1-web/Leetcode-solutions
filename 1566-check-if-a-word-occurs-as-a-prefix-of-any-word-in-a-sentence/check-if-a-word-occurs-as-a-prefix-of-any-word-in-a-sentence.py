class Solution:
    def isPrefixOfWord(self, sentence: str, word: str) -> int:
        ind=-1
        l = sentence.split()
        lenword = len(word)
        for i in l:
            if i[:lenword] == word:
                ind = l.index(i)
                break
        return ind+1 if ind!=-1 else ind