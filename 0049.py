class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sets = {}
        
        for c in strs:
            k = ''.join(sorted(c))
            if k not in sets:
                sets[k] = []
            sets[k].append(c)
        
        return [sets[k] for k in sets]
