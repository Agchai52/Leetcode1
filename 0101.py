# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    # Method 1: Recursive
    #    if not root: return True
    #    
    #    return self.mirror(root.left, root.right)
    #    
    #def mirror(self, left, right):
    #
    #    if not left or not right:
    #        return left == right
    #    if left.val != right.val:
    #        return False
    #    return self.mirror(left.left, right.right) and self.mirror(left.right, right.left)
        
    # Method 2: DFS    
        if not root:
            return True
        stackl, stackr = [root.left], [root.right]
        while len(stackl) >0 or len(stackr) > 0:
            left = stackl.pop()
            right = stackr.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stackl.append(left.left)
            stackr.append(right.right)
            stackl.append(left.right)
            stackr.append(right.left)
        return len(stackl) + len(stackr) == 0
