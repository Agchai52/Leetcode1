class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Method 1
        #for i in xrange(len(nums)-1):
        #    b = target - nums[i]
        #    l = i + 1
        #    while l < len(nums):
        #        if nums[l] == b:
        #            return [i, l]
        #        l += 1
        #return [-1, -1]
        
        # Method 2: Dictionary
        keys = {}
        for i in xrange(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
                keys[nums[i]] = i
        
