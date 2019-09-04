class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        1. for each i, cur_sum, sums = {0:-1}, sums = {cur_sum: i} only consider min(i)
        2. if cur_sum == k, max_len = i + 1
        3. if cur_sum - k in sums, max_len = max(max_len, i - sums[cur_sum-k])
        4. return max cur_sum
        
        Test case:
        [-2, -1, 2, 1], k = 1, max_len = 2
        '''
        if not nums: return 0
        cur_sum = 0
        max_len = 0
        sums = {0:-1}
        
        for i in xrange(len(nums)):
            cur_sum += nums[i]  # i = 3  cur_sum = 0
            if cur_sum not in sums: #
                sums[cur_sum] = i # sums = {0:-1, -2:0, -3:1, -1:2} 
            if cur_sum - k in sums: # cur_sum - k = 0-1 = -1
                max_len = max(max_len, i - sums[cur_sum-k]) # max_len = 2
        return max_len
    
