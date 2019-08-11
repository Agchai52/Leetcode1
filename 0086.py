# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        sroot, lroot= ListNode(0), ListNode(0)
        lroot.next = head
        hs, hb = sroot, lroot
        
        while hb:
            p = hb.next
            if p and p.val < x:
                hs.next = p
                hs = hs.next
                hb.next = p.next
                
            else:
                hb = hb.next

        hs.next = lroot.next
        
        return sroot.next
        
            
                
            
        
