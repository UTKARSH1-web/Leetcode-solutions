class Solution:
    # @return a boolean
    def isValid(self, s):
        l = []
        dict = {"]":"[", "}":"{", ")":"("}
        for s in s:
            if s in dict.values():
                l.append(s)
            elif s in dict.keys():
                if l == [] or dict[s] != l.pop():
                    return False
            else:
                return False
        return l == []