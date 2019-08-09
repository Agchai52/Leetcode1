class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    # Method 
        n = len(nums)
        i = n-1
        while i > 0 and nums[i] <= nums[i-1]: # last to first is descending
            i -= 1
        self.reverse(nums, i, n-1)
        if i > 0:
            for j in xrange(i, n):
                if nums[j] > nums[i-1]:
                    self.swap(nums, i-1, j)
                    break
        
    def reverse(self, nums, i, j):
        for k in xrange(i, (i+j)/2+1):
            self.swap(nums, k, (i+j)-k)
    
    def swap(self, nums, i, j):
        nums[j], nums[i] = nums[i], nums[j]
