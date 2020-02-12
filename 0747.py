class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 01: find max and max_idx, then check each T = O(n), S = O(1)
        '''
        if not nums: return -1
        max_val = max(nums)
        max_idx = nums.index(max_val)
        for i in range(len(nums)):
            if i == max_idx: continue
            if max_val < 2 * nums[i]: return -1
        return max_idx
        '''
        # Method 02: record first and second max then compare
        if len(nums) <= 1: return 0
        first = -1
        second = -1
        index = 0
        for i in range(len(nums)):
            if first < nums[i]:
                second = first
                first =  nums[i]
                index = i
            elif second < nums[i]:
                second = nums[i]
        if first >= second * 2:
            return index
        else:
            return -1
