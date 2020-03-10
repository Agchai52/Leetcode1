class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        
        i = 0
        while i < len(nums1):
            
            left, right = 0, len(nums2)-1 
            while left <= right and right < len(nums2):
                mid = (left + right) / 2
                
                if nums2[mid] == nums1[i]:
                    if nums1[i] not in res:
                        res.append(nums1[i])
                    nums2.remove(nums1[i])
                    nums1.remove(nums1[i])
                    i -= 1
                    break
                elif nums2[mid] < nums1[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            i += 1
        return res
        '''
        # Method 2:
        set1, set2 = set(nums1), set(nums2)
        return list(set1.intersect(set2))
        '''
