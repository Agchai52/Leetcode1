class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        nums = [1,0,1,1,0,1]
              c         0
              m       2
        '''
        if len(nums) == 0: return 0
        elif len(nums) <= 2: return sum(nums)
        
        cur_sum = 0
        max_len = 0
        
        for i in xrange(len(nums)):
            if nums[i] == 1: 
                cur_sum += 1
                max_len = max(max_len, cur_sum)
            else:
                cur_sum = 0
            
        return max_len
        
