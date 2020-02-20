class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        n = 3
        [7,3,1,0,0,6]
        [0,0,1,3,6,7]= 7
                 i
        total = 1
        '''
        nums.sort()
      
        i = 0
        total = 0
        while i < len(nums) :
            total += nums[i]
            i += 2
        return total
