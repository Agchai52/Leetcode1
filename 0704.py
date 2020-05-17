class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            val = nums[m]
            if val ==  target: 
                return m
            elif val < target: 
                l = m + 1
            else:
                r = m - 1
        return -1
