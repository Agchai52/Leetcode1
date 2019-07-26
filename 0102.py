# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
    # Method 1: DFS
    #    res = []
    #    self.level(root, res, 0)
    #    return res
    #
    #def level(self, root, res, depth):
    #    if not root: return 
    #    if depth >= len(res): # New level than new layer
    #        res.append([])
    #    res[depth].append(root.val)
    #    self.level(root.left, res, depth + 1)
    #    self.level(root.right, res, depth + 1)
        
    # Method 2: BFS
        res = []
        if not root: return res
        
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            for _ in xrange(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
            
