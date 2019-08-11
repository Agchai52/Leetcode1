# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        root = ListNode(0)
        root.next = head
        
        while head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                temp = head.next
                q = root
                head.next = head.next.next
                while q.next and q.next.val < temp.val:
                    q = q.next
                temp.next = q.next
                q.next = temp
        return root.next
