# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.is_US(root, 0)
        return self.count
    
    def is_US(self, node, val):
        if not node: return True
        if not all([self.is_US(node.left, node.val), self.is_US(node.right, node.val)]):
            return False
        self.count += 1
        return node.val == val
            
