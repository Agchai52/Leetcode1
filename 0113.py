# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sums):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
    # Method 1: PreOrder too slow
      #  if not root: return []
      #  res = []
      #  stack = []
      #  stack.append((root, ''+str(root.val)))
      #  
      #  while stack:
      #      node, path = stack.pop()
      #      if not node.left and not node.right:
      #          if eval(path) == sums:
      #              path = path.split('+')
      #              res.append([int(c) for c in path])
      #      if node.right:
      #          stack.append((node.right, path + '+' + str(node.right.val)))
      #      if node.left:
      #          stack.append((node.left, path + '+' + str(node.left.val)))
      #  return res
    
    # Method 2: Recursive
        if not root: return []
        res = []        
        self.dfs(root, sums, res, [root.val])
        return res
    
    def dfs(self, root, sums, res, path):
        if not root.left and not root.right:
            if sum(path) == sums:
                res.append(path)
                return
        if root.left:
            self.dfs(root.left, sums, res, path+[root.left.val])
        if root.right:
            self.dfs(root.right, sums, res, path+[root.right.val])
