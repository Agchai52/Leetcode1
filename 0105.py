# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left, in_right):
            if in_left > in_right: return None
            val = preorder[self.pre_i]
            self.pre_i += 1
            index = table[val]
            root = TreeNode(val)
            root.left = helper(in_left, index-1)
            root.right = helper(index+1, in_right)
            return root
        
        self.pre_i = 0
        table = {key:val for val, key in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
        
