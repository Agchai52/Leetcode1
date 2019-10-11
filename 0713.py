from collections import deque
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        prod = 1
        l, r = 0, 0
        res = 0
        while r < len(nums):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1
            res += r - l + 1 # number of subarray added after move
            r += 1
        return res
            
            
                
            
        
        
