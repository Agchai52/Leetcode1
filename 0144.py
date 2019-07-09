# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Method 1: Recursive
                
        
        #if not root: return []
        
        #res = []            
        #res.append(root.val)
        #res.extend(self.preorderTraversal(root.left))
        #res.extend(self.preorderTraversal(root.right))           
            
        #return res
        
        # Method 2: Iteration stack right then stack left
        if not root: return []
        
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res
        
