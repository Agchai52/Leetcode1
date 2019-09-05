class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''
        Method Backtrack
        1. consider n - 1 pairs since most out layer is always()
        2. pick on and pass rest       
        '''
        
        '''
         # Method 1: TLE
        if n == 0: return ['']
        if n == 1: return ['()']
        
        parents = '()' * (n-1)
        res = []
        self.dfs(parents, '', res)
        return res
    
    def dfs(self, par, path, res):
        if not par:
            path = '('+ path + ')'
            if path not in res and self.isValid(path):
                res.append(path)
            return
        for i in xrange(len(par)):
            if i > 0 and par[i-1] == par[i]:
                continue
            self.dfs(par[:i]+par[i+1:], path + par[i], res) 
            

    def isValid(self, path): 
        l, r = 0, 0
        for p in path:
            if p == '(':
                l += 1
            elif p == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        return l == 0 and r == 0
        '''
        
        # Method 2:
        if n == 0: return ['']
        if n == 1: return ['()']
        res = []
        left, right, path = n, n, ''
        self.dfs(res, left, right, path)
        return res
    
    def dfs(self, res, l, r, path):
        if l == 0 and r == 0:
            res.append(path)
            return
        if l > 0:
            self.dfs(res, l-1, r, path + '(')
        if l < r:
            self.dfs(res, l, r-1, path + ')')
            
        
