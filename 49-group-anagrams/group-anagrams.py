class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            sortword = ''.join(sorted(i))

            if sortword in d:
                d[sortword].append(i)
            else:
                d[sortword] = [i]
        ans = []
        for i in d.values():
            ans.append(i)
        return ans