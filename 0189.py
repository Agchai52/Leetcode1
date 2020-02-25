class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        # Method 1: Extra Space T=O(N), S=O(N) 
        n = len(nums)
        a = [None]*n
        for i in range(n):
            shift = (i+k) % n
            a[shift] = nums[i]
        for j in range(n):
            nums[j] = a[j]
        '''
        '''
        # Method 2: In-place, recycle T=O(N), S=O(1)
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            
            while True:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1
                if start == current: 
                    break
            start += 1
        '''
        # Method 3: reverse, T=O(n), S=O(1)
        k = k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
            
