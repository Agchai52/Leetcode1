# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        stackA, stackB = [], []
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next
            
        pre = None
        while stackA and stackB:
            a = stackA.pop()
            b = stackB.pop()
            if a != b:
                return pre
            else:
                pre = a
        return pre
