class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

       
        # Method 1: scan twice T = O(n), S = O(n)
        '''
        if not nums: return -1
        
        left_sum = [0]*len(nums)
        right_sum = [0]*len(nums)
        n = len(nums)
        for i in range(1,n):
            left_sum[i] = left_sum[i-1] + nums[i-1]
            right_sum[n-i-1] = right_sum[n-i] + nums[n-i]
            
        for i in range(n):
            if left_sum[i] == right_sum[i]:
                return i
        return -1
        '''
        # Method 2: scan once T = O(n), S = O(1)
        if not nums: return -1
        r_sum = sum(nums) - nums[0]
        l_sum = 0
        if r_sum == l_sum:
            return 0
        for i in range(1, len(nums)):
            l_sum += nums[i-1]
            r_sum -= nums[i]
            if l_sum == r_sum:
                return i
        return -1
