class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Pivot, compare mid with right
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[r]: # sorted form mid to r
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] >= nums[r]: # sorted form l to mid
                if nums[mid] > target and target >= nums[l]:
                    r = mid -1
                else:
                    l = mid + 1
        return -1
                
