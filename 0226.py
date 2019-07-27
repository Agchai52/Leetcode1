# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Method 1: Stack or PreOrder
        #if not root: return root
        #stack = []
        #stack.append(root)
        #while stack:
        #    node = stack.pop()
        #    if not node:
        #        continue
        #    node.left, node.right = node.right, node.left
        #                
        #    stack.append(node.right)
        #    stack.append(node.left)
        
        #return root
        
        # Method 2: Recursive
        if not root: 
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
        
