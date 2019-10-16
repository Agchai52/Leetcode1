class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        
        '''
        if len(nums) < 2: return len(nums)
        max_len = 1
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                cur_len = 1
                
                while cur + 1 in num_set:
                    cur += 1
                    cur_len += 1
                    
                
                max_len = max(max_len, cur_len)
        return max_len
            
            
        
