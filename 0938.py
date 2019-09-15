# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        '''
        root.left.val < root.val < root.right.val
        
        '''
        if not root: return 0
        
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.res += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        
        self.res = 0
        dfs(root)       
        return self.res
            
            
