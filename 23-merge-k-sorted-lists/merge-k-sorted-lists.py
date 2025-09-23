# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(heap,(l.val,i,l))

        dummy = ListNode()
        temp = dummy
        while heap:
            val,ind,node = heapq.heappop(heap)
            temp.next = node
            temp=temp.next
            if temp.next:
                heapq.heappush(heap,(temp.next.val,ind,temp.next))
        return dummy.next
