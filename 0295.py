from heapq import *
class MedianFinder(object):
    '''
    # Method 1: self.list.sort() O(N^2logN) TLE
    # Method 2: self.sort insert each: O(logN + N) total O(N^2)
    # Method 3: max min heap O(logN)
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        '''
        # Method 2
        self.list = []
        self.len = 0
        '''
        # Method 3
        self.minheap = []
        self.maxheap = []
        self.len = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        '''
        # Method 2
        self.len += 1
        self.sort(num)
        '''
        self.len += 1
        heappush(self.minheap, num)
        heappush(self.maxheap, -1*heappop(self.minheap))
        if len(self.maxheap) > len(self.minheap):
            heappush(self.minheap, -1*heappop(self.maxheap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        '''
        # Method 2
        #print(self.list, self.len)
        
        m = (self.len - 1) / 2
        #print(m)
        if self.len % 2 == 1:  
            return self.list[m] * 1.0
        else:
            return (self.list[m+1] + self.list[m]) / 2.0  
        '''
        if self.len % 2 == 1:
            return self.minheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2.0
        
        
        
        
    def sort(self, num):
        if len(self.list) == 0:
            self.list.append(num)
        elif num <= self.list[0]:
            self.list.insert(0, num)
        elif num >= self.list[-1]:
            self.list.insert(self.len, num)
        else:
            l = 0
            r = self.len - 1
            while l <= r:
                m = (l + r) / 2
                if num < self.list[m]:
                    r = m - 1
                else:
                    l = m + 1
            self.list.insert(l, num)     


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
