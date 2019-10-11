class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A: return 0
        res = 0
        htable = {0:1} # total:frequency
        total = 0
        m = 0
        for i in range(len(A)):
            total += A[i]
            m = total % K if K != 0 else total
            
            if m not in htable:
                htable[m] = 1
            else:
                htable[m] += 1
        # 2 C htable[m], if htable[m] >= 2
        #print(htable)
        for m in htable:
            p = htable[m]
            if p >= 2:
                res += p * (p-1) / 2
        return res
            
        
