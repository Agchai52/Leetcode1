class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1
        #i = 0
        #while i < len(nums)-1:
        #    if nums[i] < nums[i+1]:
        #        i += 1
        #    else:
        #        return i
        #return i
        
        # Mehtod 2
        left, right = 0, len(nums)-1
        while left < right:
            mid1 = (left + right) / 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                left = mid2
            else:
                right = mid1
        return left
