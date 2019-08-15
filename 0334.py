class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2: return False
        min1, min2 = float('inf'), float('inf')
        
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            elif min2 < num:
                return True
        return False
                
