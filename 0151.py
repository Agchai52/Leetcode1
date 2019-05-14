class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        for i in range(len(s)/2):
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = tmp
            
        return ' '.join(s)
