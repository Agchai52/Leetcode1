class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # Method 1: Sort and Compare O(NlogN)
        
        if len(nums) <= 1: return 0
        new = sorted(nums)
        if nums == new: return 0
        different = [i for i in range(len(nums)) if new[i] != nums[i]]
        l, r = min(different), max(different)
        return r - l + 1
        
        '''
        
        # Method 2: find min after fall and find max before rise
        if len(nums) <= 1: return 0
        
        min_, max_ = float('inf'), -float('inf')
        
        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                flag = True
            if flag:
                min_ = min(min_, nums[i])
                
        flag = False
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                flag = True
            if flag:
                max_ = max(max_, nums[i])
        
        for l in range(len(nums)):
            if min_ < nums[l]:
                break
        
        for r in range(len(nums)-1, -1, -1):
            if max_ > nums[r]:
                break
                
        return 0 if r - l < 0 else r - l + 1
            
            
        
