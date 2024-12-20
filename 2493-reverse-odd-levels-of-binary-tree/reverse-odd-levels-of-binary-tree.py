# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = []
        f=0
        q.append(root)
        # res = []
        while len(q):
            lev = []
            res = []
            for i in range(len(q)):
                el = q.pop(0)
                lev.append(el)
                res.append(el.val)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            f=f^1
            if f:
                continue     
            else:
                res = res[::-1]
                for i in range(len(res)):
                    lev[i].val = res[i]
        return root
