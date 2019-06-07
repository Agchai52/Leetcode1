class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums)-1
        

        while low < high:
            mid = (low + high) / 2
            if nums[mid] < nums[high]: 
                high = mid 
            else:
                low = mid + 1
        return nums[high]
                
