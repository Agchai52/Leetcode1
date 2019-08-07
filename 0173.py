# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext():
            if self.root:
                while self.root.left:
                    self.stack.append(self.root)
                    self.root = self.root.left
                            
                key = self.root.val
                self.root = self.root.right
            else:
                if self.stack:
                    self.root = self.stack.pop()
                    key = self.root.val
                    self.root = self.root.right            
            return key
            

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.root and not self.stack:
            return False
        return True
            
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
