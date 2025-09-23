class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        ans=[]
        heap = []
        for i in d:
            heapq.heappush(heap,(d[i],i))
            while len(heap)>k:
                heapq.heappop(heap)
        for i in heap:
            ans.append(i[1])
        return ans