# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            temp = p.next.next
            p.next.next = temp.next
            temp.next = p.next
            p.next = temp
            p = p.next.next
        return dummy.next
            
