class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Method DP1: l:[num[0], num[i-1]], r:[num[i+1], num[n-1]]
        #N = len(nums)
        #l = [1] * N
        #r = [1] * N
        #res = [None] * N
        #
        #for i in xrange(1, N):
        #    l[i] = l[i-1] * nums[i-1]
        #for i in xrange(N-2, -1, -1):
        #    r[i] = r[i+1] * nums[i+1]
        #for i in xrange(N):
        #    res[i] = l[i] * r[i]
        #return res
        
        # Method DP2:
        N = len(nums)
        l, r = 1, 1
        res = [1] * N
        for i in xrange(N):
            res[i] *= l
            res[N-i-1] *= r
            l *= nums[i]
            r *= nums[N-i-1]
        return res
        
