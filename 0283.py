class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        counter = 0
        for i in range(n):
            if nums[i] == 0:
                counter = counter + 1
            elif nums[i] != 0 and counter > 0:
                nums[i-counter] = nums[i]
                nums[i] = 0
                
        
