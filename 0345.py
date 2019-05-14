class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        v = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                v.append(i)
        for j in range(len(v)/2):
            tmp = s[v[j]]
            s[v[j]] = s[v[len(v)-j-1]]
            s[v[len(v)-j-1]] = tmp 
        
        return ''.join(s)
