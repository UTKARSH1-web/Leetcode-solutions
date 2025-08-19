# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        # print(l)
        l= [a for a in l if a < x] + [a for a in l if a>=x]
        # print(l)
        temp =head
        while temp:
            temp.val = l[0]
            l.pop(0)
            temp = temp.next
        return head
