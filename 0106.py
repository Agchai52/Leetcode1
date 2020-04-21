# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None
        if len(inorder) == 1: return TreeNode(inorder[0])
        root_val = postorder[-1]
        root = TreeNode(root_val)
        
        in_i = inorder.index(root_val)
        
        in_left, in_right = None, None
        pos_left, pos_right = None, None
               
        if in_i > 0:
            in_left = inorder[:in_i]
            len_left = len(in_left)
            pos_left = postorder[:len_left]
        if in_i + 1 < len(inorder):
            in_right = inorder[in_i+1:]
            len_right = len(in_right)
            pos_right = postorder[-1-len_right:-1]
                 
        root.left = self.buildTree(in_left, pos_left)
        root.right = self.buildTree(in_right, pos_right)
        return root
