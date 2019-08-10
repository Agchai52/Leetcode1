# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            # cut it in half    
            head1 = head
            head2 = slow.next
            slow.next = None
            
            # reverse linked list head2     
            #dummy = ListNode(0)
            #dummy.next = head2
            #p = head2.next
            #head2.next = None
            #while p:
            #    temp = p
            #    p = p.next
            #    temp.next = dummy.next
            #    dummy.next = temp
            #head2 = dummy.next
            h = head2
            newHead = None
            while h:
                p = h
                h = h.next
                p.next = newHead
                newHead = p
            head2 = newHead

            # merge 
            p1 = head1
            p2 = head2
            while p2:
                tmp1 = p1.next
                tmp2 = p2.next
                p1.next = p2
                p2.next = tmp1
                p1 = tmp1
                p2 = tmp2
            
            
    
    
