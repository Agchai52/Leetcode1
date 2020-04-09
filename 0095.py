# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0: return []    
        return self.generateBST(1, n)
        
    def generateBST(self, start, end):
        if start > end: return [None]
        res = []
        for i in range(start, end+1):           
            left_trees = self.generateBST(start, i-1)
            right_trees = self.generateBST(i+1, end)
            
            for l in left_trees:
                for r in right_trees:
                    cur = TreeNode(i)     
                    cur.left = l 
                    cur.right = r 
                    res.append(cur)            
        return res
