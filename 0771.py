class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # Method 1: Hash table
        if not S or not J: return 0
        smap = collections.Counter(S)
        res = 0
        for j in J:
            if j in smap:
                res += smap[j]
        return res
            
