# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Method 1
        #if not head or not head.next or k == 0: return head
        #_len = 0
        #root = head
        #while head:
        #    _len += 1
        #    head = head.next
        #
        #k %= _len
        #if k == 0: return root
        #
        #pre = slow = fast = root
        #while k > 1:
        #    fast = fast.next
        #    k -= 1
        #
        #while fast.next:
        #    fast = fast.next
        #    pre = slow
        #    slow = slow.next
        #    
        #    
        #pre.next = None
        #fast.next = root
        #
        #return slow
    
        # Method 2: loop
        if not head or not head.next or k == 0: return head
        _len = 0
        root = head
        preH = head
        while head:
            preH = head
            _len += 1
            head = head.next
        
        k %= _len
        if k == 0: return root
        
        step = _len-k
        pre = cur = root
        preH.next = root
        
        while step > 0:
            pre = cur
            cur = cur.next
            step -= 1
        
        pre.next = None
        return cur
