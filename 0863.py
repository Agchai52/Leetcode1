# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        '''
        1. distance K start from target
        2. distarce K-L from root: L is distance from root to target
        
        '''
        # Method 1: Max recursion depth exceeded
        '''
        if not root or not target: return []
        if K == 0 and root.val == target.val: return [root.val]
        if K == 0 and root.val != target.val: return []
        
        res = []
        
        # Distance from node to target, not find return -1
        def dfs(node):
            if not node:
                return -1
            if node == target:
                subtree_add(node, 0)
                return 1
            
            L, R = dfs(root.left), dfs(root.right)
            if L != -1:
                if L == K: res.append(node.val)
                else: subtree_add(node.right, L + 1)
                return L + 1
            elif R != -1:
                if R == K: res.append(node.val)
                else: subtree_add(node.left, R + 1)
                return R + 1
            else:
                return -1
       
        # Add all nodes 'K - dist' from node to answer    
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                res.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)
                    
        
        dfs(root)
        return res
        '''
        
        # Method 2: add par to each node
        # add par to each node
        def dfs(node, par = None):
            if not node: return
            node.par = par
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root)
        que = collections.deque([(target, 0)])
        seen = set()
        seen.add(target)
        while que:
            if que[0][1] == K:
                return [node.val for node, d in que]
            node, d = que.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    que.append((nei, d+1))
            
        return []
        
        
        
        
        
        
        
        
