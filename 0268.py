class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # Method1: NlogN       
        nums.sort()
        if nums[0] != 0: return 0
        n = len(nums)
        for i in xrange(n):
            if nums[i] != i:
                return i
        return n
        '''
        
        '''
        # Method2: Hash set O(N)
        d = set(nums)
        n = len(nums)
        for i in xrange(n):
            if i not in d:
                return i
        return n
        
        '''
        '''
        # Method 3: sum O(N)
        n = len(nums)
        total = n * (n+1) / 2
        return total - sum(nums)
        '''
        
        # Method 4: Bit manipulation O(N)
        n = len(nums)
        res = n
        for i in xrange(n):
            res ^= i
            res ^= nums[i]
        return res
        
        
