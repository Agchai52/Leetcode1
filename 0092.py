# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
       
        
        if not head or m == n:
            return head
        dummy = ListNode('#')
        dummy.next = head
        prev = dummy
        
        for _ in range(m-1):
            prev = prev.next
            
        start, end = prev.next, prev.next
        for _ in range(m-1,n):
            end = end.next
    
        for _ in range(m-1,n):
            next_ = start.next
            
            start.next = end
            
            end = start
            
            start = next_
            
        
        prev.next = end
        if m == 1:
            head = end
        return head
