# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Method 1
        #if not head or not head.next: return True
        #array = []
        #while head:
        #    array.append(head.val)
        #    head = head.next
        #for i in xrange(len(array)/2+1):
        #    if array[i] != array[len(array)-i-1]:
        #        return False
        #return True
    
        # Method 2: Time O(n) and Space O(1)
        if not head or not head.next: return True
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        slow = slow.next
        slow = self.reverseLink(slow) # reverse second half of link
        
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True
    
    def reverseLink(self, head):
        newHead = None
        while head:
            p = head
            head = head.next # Important!
            p.next = newHead
            newHead = p
            
        return newHead
