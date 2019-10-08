class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # https://blog.csdn.net/fuxuemingzhu/article/details/79234075
        res = []
        s = ''.join(S.split('-')).upper()
        N = len(s)
        if N % K != 0:
            res.append(s[:N%K])
        for i in range(N%K, N, K):
            res.append(s[i:i+K])
        return '-'.join(res)
        
                
        
        
