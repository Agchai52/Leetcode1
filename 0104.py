# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Method 1: DFS
        #if not root: return 0
        #return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
        # Method 2: BFS
        if not root: return 0
        depth = 0
        q = [root]
        while len(q) != 0:
            depth += 1
            for _ in range(len(q)):
                node = q.pop(0)
                if not node.left and not node.right:
                    continue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth
                
        
        
