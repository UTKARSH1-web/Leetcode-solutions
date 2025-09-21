# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft() # deque.popleft() is much faster
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")
        # print(result)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')
        # print(l)
        i=0
        if l==['']:
            return None
        root = TreeNode(int(l[i]))
        q= deque([root])
        i=1
        while q:
            parent = q.popleft()
            if l[i]!='#':
                left = TreeNode(int(l[i]))
                q.append(left)
                parent.left = left
            i+=1
            if l[i]!='#':
                right =TreeNode(int(l[i]))
                parent.right=right
                q.append(right)
            i+=1
        # print(root)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))