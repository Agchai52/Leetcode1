# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return '[]'
        res = [str(root.val)]
        q = [root]        
        while q:            
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            res.append(str(node.left.val) if node.left else 'null')
            res.append(str(node.right.val) if node.right else 'null')
        while res and res[-1] == 'null':
            res.pop()
        return '[' + ','.join(res) + ']'
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return None
        nums = data[1:-1].split(',')
        root = TreeNode(int(nums.pop(0)))
        q = [root]
        while len(q) != 0 and len(nums) !=0:
            cur = q.pop(0)
            val = nums.pop(0)
            if val != 'null':
                node = TreeNode(int(val))
                q.append(node)
                cur.left = node
            if len(nums) !=0:
                val = nums.pop(0)
            else:
                break
            if val != 'null':
                node = TreeNode(int(val))
                q.append(node)
                cur.right = node
        return root
       
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
