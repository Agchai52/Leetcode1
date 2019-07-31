# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sums):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
    # Method 1: PreOrder
    #    if not root: return False
    #    stack = []
    #    stack.append((root, root.val))        
    #    while stack:
    #        node, path = stack.pop()
    #        if not node.left and not node.right:
    #            if path == sums:
    #                return True
    #        if node.right:
    #            stack.append((node.right, path + node.right.val))             
    #        if node.left:
    #            stack.append((node.left, path + node.left.val))            
    #    return False
    
    # Method 2: Recusive
        if not root: return False
        if not root.left and not root.right:
            return sums == root.val
        return self.hasPathSum(root.left, sums - root.val) or self.hasPathSum(root.right, sums - root.val)
            
   
        
        
