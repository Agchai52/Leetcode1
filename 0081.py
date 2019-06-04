class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # Compared to 33, shift left only
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            while l < r and nums[l] == nums[r]:
                l += 1
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
