# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
    # Method 1: PreOrder
        #res = []
        #if not root:
        #    return res
        #stack = []
        #stack.append(root)
        #path = []
        #
        #while stack:
        #    node = stack.pop()
        #    if not node:
        #        continue
        #    if node == '0': # end of branch
        #        path = path[:-1]
        #        continue
        #        
        #    if not node.left and not node.right and node.val:  # leaf         
        #        path.append(node.val) 
        #        temp = '->'.join([str(i) for i in path])
        #        res.append(temp)
        #        path = path[:-1]
        #        continue
        #    
        #    
        #    path.append(node.val) 
        #    
        #    stack.append('0') # end of branch
        #    stack.append(node.right)
        #    stack.append(node.left)
        #    print stack
        #return res
        
    # Method 2: Recursive
    #    res = []
    #    if not root: return res
    #    self.dfs(root, res, ''+str(root.val))
    #    return res
    #    
    #def dfs(self, root, res, path):
    #    if not root.left and not root.right:
    #        res.append(path)
    #    if root.left:
    #        self.dfs(root.left, res, path + '->' + str(root.left.val))
    #    if root.right:
    #        self.dfs(root.right, res, path + '->' + str(root.right.val))
        
    # Method 3: PreOrder 2, right first and then left
        if not root: return []
        res = []
        stack = []
        stack.append((root, str(root.val)))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
        return res
