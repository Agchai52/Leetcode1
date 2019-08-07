# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
 # Method 1: DFS
 #       if not root: return True
 #       if abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1:
 #           return self.isBalanced(root.left) and self.isBalanced(root.right)
 #       else:
 #           return False
 #       
 #       
 #   def getDepth(self, node):
 #       if not node:
 #           return 0
 #       return 1 + max(self.getDepth(node.left), self.getDepth(node.right))
 
 # Method 2: reset value then DFS
        if not root: return True
        self.getAllDepth(root)
        left_depth = root.left.val if root.left else 0
        right_depth = root.right.val if root.right else 0
        
        if abs(left_depth - right_depth) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
    def getAllDepth(self, root):
        if not root: return 0
        root.val = 1 + max(self.getAllDepth(root.left), self.getAllDepth(root.right))
        return root.val
        
