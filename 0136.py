class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1: Bit
        #return reduce(lambda x, y: x^y, nums)
        
        # Method 2
        res = 0
        for i in nums:
            res ^= i
        return res
