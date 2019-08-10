# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next: return None
        root = ListNode(0)
        root.next = head
        pre = root
        stack = []
        while pre.next:
            stack.append(pre.next)
            pre = pre.next
        
        node = stack[-n]
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            node_pre = stack[-1-n]
            node_pre.next = None
        return root.next
