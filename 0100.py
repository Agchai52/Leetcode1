# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # Method 1: Preorder Tree or stack.append((p,q))
        #if not p and not q:
        #    return True
        #if (not p and q) or (p and not q):
        #    return False
        #
        #stackp = []
        #stackq = []
        #
        #stackp.append(p)
        #stackq.append(q)
        #while stackp and stackq:
        #    nodep = stackp.pop()
        #    nodeq = stackq.pop()
        #    if not nodep and not nodeq:
        #        continue
        #    elif (not nodep and nodeq) or (nodep and not nodeq):
        #        return False
        #    if nodep.val != nodeq.val:
        #        return False
        #    else:
        #        stackp.append(nodep.right)
        #        stackp.append(nodep.left)
        #        
        #        stackq.append(nodeq.right)
        #        stackq.append(nodeq.left)
        #        
        #return True
        
        # Method 2: DFS
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
        return p == q
