class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0        
        res = 1
        l, r = 0, 1
        while r < len(nums):
            if nums[r-1] < nums[r]:
                res = max(res, r-l+1)
                r += 1
            else:
                l = r
                r = r + 1
        return res
            
        
