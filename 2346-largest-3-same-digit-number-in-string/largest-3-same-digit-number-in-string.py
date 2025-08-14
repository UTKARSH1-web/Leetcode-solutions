class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        m=''
        for i in range(n-2):
            sub=num[i:i+3]
            if sub.count(sub[0])==3:
                # print(sub)
                m=max(m,sub)
        return str(m)