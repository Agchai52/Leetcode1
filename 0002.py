# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2
        root = ListNode(0)
        pre = root
        flag = 0
        while head1 or head2:
            if head1:
                a = head1.val
            else:
                a = 0
            
            if head2:
                b = head2.val
            else:
                b = 0
            
            c = a + b + flag
            if c >= 10:
                flag = 1
                c -= 10
            else:
                flag = 0
            pre.next = ListNode(c)
            
            pre = pre.next
            if not head1.next and head2.next:
                head1.next = ListNode(0)
            elif not head2.next and head1.next:
                head2.next = ListNode(0)
            
            head1 = head1.next
            head2 = head2.next
        
        if flag != 0:
            pre.next = ListNode(flag)
            
        return root.next
        
