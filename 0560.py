class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        res = 0
        n = len(nums)
        # Method 1: Brute Force TLE        
        #sums = [0] * n
        #sums[0] = nums[0]
        #for i in range(1, n):
        #    sums[i] = sums[i-1] + nums[i]
        #for i in range(n):
        #    for j in range(i, n):
        #        summ = sums[j] - sums[i] + nums[i]
        #        if summ == k:
        #            res += 1
        #return res
        
        # Method 2: Brute Force set sum = 0 for each new i 
        
        # Method 3: Hash Table
        
        table = collections.defaultdict(int)
        table[0] = 1
        total = 0
        for i in range(n):
            total += nums[i]
            if total - k in table:
                res += table[total-k]
            table[total] += 1
        return res
