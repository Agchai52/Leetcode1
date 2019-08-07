# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        flag = 0
        res = []
        q = [root]
        
        while len(q) != 0:
            flag += 1
            level = []
            for _ in xrange(len(q)):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if flag % 2 == 1:
                res.append(level)
            else:
                res.append(level[::-1])
        return res
