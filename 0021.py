# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: return None
        root = ListNode(0)
        pre = root
        
        while l1 and l2:
            a = l1.val
            b = l2.val
            if a < b:
                pre.next = ListNode(a)
                l1 = l1.next
            elif a > b:
                pre.next = ListNode(b)
                l2 = l2.next
            elif a == b:
                pre.next = ListNode(a)
                pre = pre.next
                pre.next = ListNode(b)
                l1 = l1.next
                l2 = l2.next
            pre = pre.next
        
        if l1:
            pre.next = l1
        elif l2:
            pre.next = l2
        
        return root.next
