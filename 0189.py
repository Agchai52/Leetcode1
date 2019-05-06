class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [None]*n
        for i in range(n):
            shift = (i+k) % n
            a[shift] = nums[i]
        for j in range(n):
            nums[j] = a[j]
