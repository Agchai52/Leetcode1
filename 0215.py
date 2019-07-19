class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Method 1: Sort O(nlogn)
        #nums.sort()
        #n = len(nums)
        #return nums[n - k]
         
        # Method 2: Max heap O(n + klogn)
        #import heapq
        #nums = [-num for num in nums] # min heap to max heat
        #heapq.heapify(nums)
        #for _ in xrange(k):
        #    res = heapq.heappop(nums)
        #return -res 
        
        # Method 3: Min heap O(k) + O((n-k)logk)
        import heapq
        min_heap = [-float('inf')] * k
        heapq.heapify(min_heap)
        for num in nums:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
        return min_heap[0]
