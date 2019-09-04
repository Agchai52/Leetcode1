from heapq import *
class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''
        Method : max heap and min heap
        1. min heap: right half of total array 
        2. max heap: left half of total array
        3. len(min) == len(max), even, average top of min and max
        4. len(min) == len(max) + 1, odd, top of min
        5. max = [-num]
        '''
        m, n = len(num1), len(num2)
        if m == 0 and n == 0: return None
        minheap = num1
        maxheap = []
        while len(minheap) - len(maxheap) > 1:
            heappush(maxheap, -heappop(minheap))
        
        for val in num2:
            heappush(minheap, val)
            heappush(maxheap, -heappop(minheap))
            if len(maxheap) > len(minheap):
                heappush(minheap, -heappop(maxheap))
                
        if (m+n) % 2 == 1:
            return float(minheap[0])
        else:
            return (minheap[0]-maxheap[0]) / 2.0
        '''
        num1 = [1, 3]
        num2 = [2]
        
        min = [2, 3]
        max = [-1]
        '''
