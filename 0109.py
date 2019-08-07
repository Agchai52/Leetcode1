# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.dfs(nums, 0, len(nums)-1)
    
    def dfs(self, nums, left, right):
        if left <= right:
            mid = (left + right) / 2
            root = TreeNode(nums[mid])
            root.left = self.dfs(nums, left, mid-1)
            root.right = self.dfs(nums, mid+1, right)
            return root
