class Solution:
    def insert(self, inter: List[List[int]], new: List[int]) -> List[List[int]]:
        # intervals.insert(1,new)
        if len(inter)==0:
            return [new]
        for i in range(len(inter)):
            if inter[i][0]<= new[0]:
                inter.insert(i+1,new)
                break
            else:
                inter.insert(i,new)
                break
        inter.sort()
        # print(inter)
        
        ans=[]
        temp = inter[0]
        for i in inter:
            if i[0]<=temp[1]:
                temp[1] = max(temp[1],i[1])
            else:
                ans.append(temp)
                temp = i
        ans.append(temp)
            # print(temp)
        return ans
