class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        
        for i in xrange(2, int(n ** 0.5) + 1):
            if primes[i] == 1:
                for j in xrange(i+i, n, i):
                    primes[j] = 0
        
        
        return sum(primes)
