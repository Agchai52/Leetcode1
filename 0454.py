class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        table = collections.defaultdict(int)
        
        for a in A:
            for b in B:
                table[a+b] += 1
        
        return sum(table[-c-d] for c in C for d in D)
