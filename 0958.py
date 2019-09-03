# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    # Method 1:
        '''
        1. get height of tree
        2. befor last level, all full
        3. at last level, no None before end
        4. not root?
        '''
        '''
        if not root: return False
        height = self.getHeight(root)
        q = [root]
        level = 1
        last = []
        while q and level < height:
            for _ in range(len(q)):
                node = q.pop(0)
                if not node:
                    return False
                q.append(node.left)
                q.append(node.right)
            level += 1
        while q:
            last.append(q.pop(0))
        return self.isAllLeft(last)
    
    def getHeight(self, node):
        if not node: return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        return max(left, right) + 1
    
    def isAllLeft(self, last):
        n = len(last)
        i = n-1
        while i >= 0 and last[i] == None:
            i -= 1
        while i >= 0:
            if last[i] == None:
                return False
            i -= 1
        return True
    '''

        # Method 2: BFS
        que = [(root, 1)]
        i = 0
        while i < len(que):
            node, v = que[i]
            i += 1
            if node:
                que.append((node.left, 2*v))
                que.append((node.right, 2*v+1))
        return que[-1][1] == len(que)
        
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def list2Tree(array):
    root = TreeNode(array[0])
    queue = [root]
    index = 1
    while index < len(array):
        node = queue.pop(0)
        
        val = array[index]
        index += 1
        
        if val != None:
            node.left = TreeNode(val)
            queue.append(node.left)
        
        if index >= len(array):
            break
        
        val = array[index]
        index += 1
        
        if val != None:
            node.right = TreeNode(val)
            queue.append(node.right)
    return root
    
if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    root = list2Tree(nums)
    sol = Solution()
    print(sol.isCompleteTree(root))
