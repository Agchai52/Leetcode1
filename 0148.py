# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        pre = slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None # Make second half of head == None
        
        l1 = self.sortList(head) # first half
        l2 = self.sortList(slow) # second half
        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        move = head
        if not l1: return l2
        if not l2: return l1
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2
        return head.next
