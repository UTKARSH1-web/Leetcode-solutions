class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()
        temp = intervals[0]
        for i in intervals:
            if i[0]<=temp[1]:
                temp[1]= max(i[1],temp[1])
            else:
                merged.append(temp)
                temp = i
        merged.append(temp)
        return merged