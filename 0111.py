# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Method 1: BFS
        #if not root: return 0
        #depth = 0        
        #q = [root]
        #while len(q)!= 0:
        #    depth += 1
        #    for _ in xrange(len(q)):
        #        node = q.pop(0)
        #        if not node.left and not node.right:
        #            return depth
        #        if node.left:
        #            q.append(node.left)
        #        if node.right:
        #            q.append(node.right)
                    
        # Method 2: DFS
        if not root: return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            
