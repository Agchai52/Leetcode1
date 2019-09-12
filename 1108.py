class Solution(object):
    def defangIPaddr(self, s):
        """
        :type address: str
        :rtype: str
        """
        return s.replace('.','[.]')
