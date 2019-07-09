# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Method 1: Recursive
        #if not root: return []
        #
        #res = []
        #
        #res.extend(self.inorderTraversal(root.left))
        #res.append(root.val)
        #res.extend(self.inorderTraversal(root.right))
        #
        #return res
        
        # Method 2: Iterative by Stack
        if not root: return []
        
        res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right
        
        
