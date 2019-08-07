# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Method 1: Bfs
        if not root: return []
        res = []
        queue = [root]
        while len(queue) != 0:
            level = []
            for _ in xrange(len(queue)):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            res.append(level)
        return res[::-1]
