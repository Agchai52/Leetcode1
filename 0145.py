# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Method 1: Recursive
        #if not root: return []
        #
        #res = []
        #res.extend(self.postorderTraversal(root.left))
        #res.extend(self.postorderTraversal(root.right))
        #res.append(root.val)
        #
        #return res
        
        # Method 2: Iterative by Stack: inverse(root, right, left)
        if not root: return []
        
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return res[::-1]
