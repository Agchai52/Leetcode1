# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        root = ListNode(float('inf'))
        root.next = head
        pre = root
        val = float('inf')
        while pre and pre.next:
            p = pre.next
            if p.next and p.val == p.next.val:
                val = p.val
                pre.next = p.next
                p = pre.next
                if p.next and p.next.val != val:
                    pre.next = p.next
                    val = float('inf')
                elif not p.next and val != float('inf'):
                    pre.next = p.next
            else:
                pre = pre.next
        return root.next
                
            
        
