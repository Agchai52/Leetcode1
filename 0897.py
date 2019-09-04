# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        '''
        1. in-order Traversal
        2. generate new tree at the same time
        3. Time O(N) Space O(N)
        '''
        '''
        # Method 1: Stack
        if not root or not root.left and not root.right: return root
        stack = []
        head = pointer = TreeNode(0)
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return head.right
            root = stack.pop()
            pointer.right = TreeNode(root.val)
            pointer = pointer.right
            root = root.right
        return head.right
        '''
        
        # Method 2: Recursion
        if not root or not root.right and not root.left: return root
        head = TreeNode(0)
        self.point = head
        self.dfs(root)
        return head.right
    
    def dfs(self, root):
        if not root: return None        
        self.dfs(root.left)
        self.point.right = TreeNode(root.val)
        self.point = self.point.right
        self.dfs(root.right)
        
        
            
        
        
