# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, float('-inf'), float('inf'))
    
    def valid(self, node, minv, maxv):
        if not node: return True
        if node.val <= minv or node.val >= maxv:
            return False
        return self.valid(node.left, minv, node.val) and self.valid(node.right, node.val, maxv)
                    
