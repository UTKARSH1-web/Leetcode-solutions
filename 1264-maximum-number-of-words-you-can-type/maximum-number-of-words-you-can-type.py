class Solution:
    def canBeTypedWords(self, text: str, lett: str) -> int:
        return len(text.split())- sum(any(letter in word for letter in lett) for word in text.split())
