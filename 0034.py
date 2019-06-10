class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]
        
        left, right = 0, len(nums)-1
        
        # Method 1
        #while left <= right:
        #    mid = (left + right) / 2
        #    if nums[mid] == target:
        #        while nums[left] != target:
        #            left += 1
        #        while nums[right] != target:
        #            right -= 1
        #        return [left, right]
        #    elif nums[mid] < target:
        #        left = mid + 1
        #    else:
        #        right = mid - 1
        #return [-1, -1]
        
        # Method 2
        while left <= right:
            mid = (right + left) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left, right = mid, mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < len(nums)-1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
        return [-1, -1]
