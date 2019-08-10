# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return head
        
        root = ListNode(0)
        root.next = head
        pre = root
        
        while pre:
            p = pre.next
            
            if p and p.val == val: 
                
                pre.next = p.next
            else:
                pre = pre.next
        return root.next
                
