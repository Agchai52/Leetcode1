# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Method 1: Brute Force Time = O(NlogN) Space = O(N)
        #nodes = []
        #head = point = ListNode(0)
        #for l in lists:
        #    while l:
        #        nodes.append(l.val)
        #        l = l.next
        #for x in sorted(nodes):
        #    point.next = ListNode(x)
        #    point = point.next
        #return head.next
        
        # Method 2: Heapq Time = O(NlogK) Space = O(N),
        import heapq
        head = point = ListNode(0)
        q = []
        for l in lists:
            if l:
                q.append((l.val, l))
        heapq.heapify(q)
        while len(q) != 0:
            val, node = heapq.heappop(q)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(q, (node.val, node))
        return head.next
'''
if __name__ = '__main__':
    lists = [[1], [1,2], [2,3,4]]
    print(Solution().mergeKLists(lists))
'''
