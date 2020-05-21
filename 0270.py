# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        a = root.val
        child = root.left if target < a else root.right
        if not child: return a
        b = self.closestValue(child, target)
        return min((a, b), key = lambda x: abs(x-target))
