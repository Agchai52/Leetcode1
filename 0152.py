class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1: Bruth Force (TLE)
        #res = float('-inf')
        #n = len(nums)
        #for i in xrange(n):
        #    cur = 1
        #    for j in xrange(i, n):
        #        cur *= nums[j]
        #        res = max(res, cur)
        #return res
        
        # Method 2: DP: record max prod and min prod 
        #if not nums: return 0
        #N = len(nums)
        #prod_min = [0] * N
        #prod_max = [0] * N
        #prod_min[0] = prod_max[0] = res = nums[0]
        #for i in xrange(1, N):
        #    prod_min[i] = min(prod_min[i-1]*nums[i], nums[i], prod_max[i-1]*nums[i])
        #    prod_max[i] = max(prod_min[i-1]*nums[i], nums[i], prod_max[i-1]*nums[i])
        #    res = max(res, prod_max[i])     
        #return res
        
        # Method 3: Simplied 2
        #if not nums: return 0
        #N = len(nums)
        #prod_min = prod_max = res = nums[0]
        #for i in xrange(1, N):
        #    pre_min = prod_min
        #    pre_max = prod_max
        #    prod_min = min(pre_min*nums[i], nums[i], pre_max*nums[i])
        #    prod_max = max(pre_min*nums[i], nums[i], pre_max*nums[i])
        #    res = max(res, prod_max)
        #return res
    
        # Method 4: Simplied 3
        if not nums: return 0
        N = len(nums)
        prod_min = prod_max = res = nums[0]
        for i in xrange(1, N):
            if nums[i] < 0:
                prod_min, prod_max = prod_max, prod_min
            prod_min, prod_max = min(prod_min*nums[i], nums[i]), max(nums[i], prod_max*nums[i])
            res = max(res, prod_max)
        return res
