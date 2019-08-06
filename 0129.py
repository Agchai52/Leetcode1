# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Method 1: PreOrder
        #if not root: return 0
        #nums = []
        #stack = []
        #stack.append((root, root.val))
        #while stack:
        #    node, num = stack.pop()
        #    if not node.left and not node.right:
        #        nums.append(num)
        #    if node.right:
        #        stack.append((node.right,  num*10 + node.right.val))
        #    if node.left:
        #        stack.append((node.left, num*10 + node.left.val))             
        #return sum(nums)
    
    # Method 2: Recursive:
        if not root: return 0
        res = []
        self.dfs(root, root.val, res)
        return sum(res)
    
    def dfs(self, node, num, res):
        if not node.left and not node.right:
            res.append(num)
        if node.left:
            self.dfs(node.left, num*10 + node.left.val, res)
        if node.right:
            self.dfs(node.right, num*10 + node.right.val, res)
