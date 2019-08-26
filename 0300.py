class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://blog.csdn.net/aliceyangxi1987/article/details/50478794
        # Method 1: DP Brute Force
        #if not nums: return 0
        #
        #l = len(nums)
        #dp = [1] * l
        #for i in range(l):
        #    for j in range(i):
        #        if nums[j] < nums[i]:
        #            dp[i] = max(dp[i], dp[j]+1)
        #return max(dp)
    
        # Method 2: DP + Binary Search
        if not nums: return 0
        l = len(nums)
        ans = []
        for x in nums:
            low = 0
            high = len(ans) - 1
            # Detect location of x inside list ans
            while low <= high:
                mid = (low + high) / 2
                if ans[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            if low >= len(ans):
                ans.append(x)
            else:
                ans[low] = x
        return len(ans)
            
        
        
