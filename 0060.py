class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # https://blog.csdn.net/fuxuemingzhu/article/details/80658810
        res = ''
        factor = [1] * n
        num = [str(i+1) for i in xrange(9)]
        for i in xrange(1, n): # compute 1! ~ (n-1)!
            factor[i] = factor[i-1] * i
        
        k -= 1
        for i in xrange(n, 0, -1):
            first = k // factor[i-1] 
            k %= factor[i-1]
            res += num[first]
            num.pop(first)
        
        return res
