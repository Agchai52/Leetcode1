# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxsum = float('-inf')
        self.postTraversal(root)
        return self.maxsum
    
    def postTraversal(self, root):
        if not root:
            return 0
        left = self.postTraversal(root.left)
        right = self.postTraversal(root.right)
        left_max = left if left > 0 else 0 # if negative, don't go through
        right_max = right if right > 0 else 0
        self.maxsum = max(self.maxsum, left_max + right_max + root.val)
        return max(left_max, right_max) + root.val
'''
if __name__ == '__main__':
    input = [-10,9,20,null,null,15,7]
    root = list2tree(input) # inOrderTraversals()
    print(Solution().maxPathSum(root))
'''
