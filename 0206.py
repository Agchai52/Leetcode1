# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Method 1: Iteration
        #if head == None or head.next == None: return head
        #
        #newHead = None
        #while head != None:
        #    temp = head.next
        #    head.next = newHead
        #    newHead = head
        #    head = temp
        #return newHead
        
        # Method 2: Iteration
        #if not head or head.next == None: return head
        #dummy = ListNode(-1)
        #while head:
        #    temp = head.next
        #    head.next = dummy.next
        #    dummy.next = head
        #    head = temp
        #return dummy.next
        
        # Method 3: Recursion
        return self.reverse(head, None)
    
    def reverse(self, head, newHead):
        if not head:
            return newHead
        oldNext = head.next
        head.next = newHead
        return self.reverse(oldNext, head)
        
