class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for c in s:
            if c in letters:
                letters[c] = letters[c] + 1
            else:
                letters[c] = 1
        print(letters)
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1
