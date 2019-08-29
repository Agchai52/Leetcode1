class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Method 1: Hash Table
        #if not s: return 0
        #n = len(s)
        #d = collections.Counter(s)
        #extra = 0
        #for k in d:
        #    if d[k] % 2 == 1:
        #        extra += 1
        #if extra == 0: return n
        #else: return n-extra+1
        
        # Method 2: stack
        if not s: return 0
        n = len(s)
        s = [ord(c) for c in s]
        s.sort()
        stack = [s[0]]
        for i in range(1, n):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        if not stack: return n
        else: return n - len(stack) + 1
    
