class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: return ['']
        
        # Check if s is valid
        if self.isValid(s): 
            return [s]
        
        # If it's not valid, compute num of invalid '(' and ')'
        l, r = self.invalidNum(s)
        
        # DFS, remove invalid parentheses
        res = []
        self.dfs(s, 0, l, r, res)
        return res
    
    def dfs(self, s, index, l, r, res):
        if l == 0 and  r == 0 and self.isValid(s):
            res.append(s)
            return
        
        for i in xrange(index, len(s)):
            if i > index and s[i] == s[i-1]:
                continue
            if s[i] == ')' and r > 0:
                self.dfs(s[:i]+s[i+1:], i, l, r-1, res)
            elif s[i] == '(' and l > 0:
                self.dfs(s[:i]+s[i+1:], i, l-1, r, res)
    
    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(': count += 1
            elif c == ')': count -= 1
            if count < 0: return False
        return count == 0
    
    def invalidNum(self, s):
        l, r = 0, 0
        for c in s:
            if c == '(': 
                l += 1
            if c == ')':   
                if l == 0: r += 1
                else: l -= 1
        return l, r
        
        
        
