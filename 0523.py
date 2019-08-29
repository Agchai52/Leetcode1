class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        k = 0, nums[i] = 0
        k = 1, all subarray of nums
        sum(subarray) % 4 = 0
        '''
        if len(nums) < 2: return False
        n = len(nums)
        
        
        # Method 1: Brute Force
        #sums = [0] * n
        #sums[0] = nums[0]
        #for i in range(n):
        #    sums[i] = sums[i-1] + nums[i]
        #
        #for i in range(n-1):
        #    for j in range(i+1, n):
        #        summ = sums[j] - sums[i] + nums[i]
        #        if summ == k or k!=0 and summ % k == 0:
        #            return True
        #return False
                
        # Method 2: Hash Table
        # http://bookshadow.com/weblog/2017/02/26/leetcode-continuous-subarray-sum/
        # if k!=0 and a % k == b % k, then (a-b) % k = 0
        # Also, for two index of the same mod, their difference has to be more than 2
        table = {0: -1}
        total = 0
        for i, t in enumerate(nums):
            total += t
            m = total % k if k != 0 else total
            if m not in table: 
                table[m] = i
            else:
                if table[m] < i-1:
                    return True
        return False
            
