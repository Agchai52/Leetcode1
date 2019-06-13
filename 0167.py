class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Method 1: same as #1
        
        # Method 2: Binary
        nums = numbers
        for i in xrange(len(nums)-1):
            b = target - nums[i]
            l, r = i + 1, len(nums)-1
            while l <= r:
                m = (l + r) / 2
                if nums[m] == b:
                    return [i+1,m+1]
                elif nums[m] < b:
                    l = m + 1
                else:
                    r = m - 1
        return [-1,-1]
        
        # Method 3: Binary from edge to middle
        nums = numbers
        l, r = 0, len(nums)-1
        while l < r:
            n_m = nums[r] + nums[l]
            if n_m == target:
                return [l + 1, r + 1]
            elif n_m < target:
                r = r - 1
            else:
                l = l + 1
        return [-1, -1]
