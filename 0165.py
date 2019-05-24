class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        length = len(v1) if len(v1)<=len(v2) else len(v2)
        
        for i in xrange(length):
            if int(v1[i]) == int(v2[i]):
                continue
            elif int(v1[i]) > int(v2[i]):
                return 1
            else:
                return -1
        
        if len(v1) > len(v2) and int(v1[-1]) != 0 :
            return 1
        elif len(v1) < len(v2) and int(v2[-1]) != 0 :
            return -1
        else:
            return 0
