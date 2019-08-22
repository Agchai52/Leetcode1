# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Method 1: BFS + Dict
        if not root: return []
        column = dict()
        q = [(root, 0)]
        while q:
            for _ in q:
                node, col = q.pop(0)
                if col in column:
                    column[col].append(node.val)
                else:
                    column[col] = [node.val]
                if node.left:
                    q.append((node.left, col-1))
                if node.right:
                    q.append((node.right, col+1))
        res = []
        for c in sorted(column.keys()):
            res.append(column[c])
        return res
                
