class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        if len(A) == 1: return 1
        if len(A) == 2: return 2
        
        dic = collections.defaultdict(list)
        res = 0
        
        for i, v in enumerate(A):
            dic[v].append(i)
            
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                count = 2
                diff = A[j] - A[i]
                next = A[j] + diff
                min_idx = j
                while True:
                    if next not in dic: break
                    if min_idx >= dic[next][-1]: break
                    for list_i in range(len(dic[next])):
                        if dic[next][list_i] > min_idx:                       
                            break
                    if list_i == len(dic[next]):
                        break
                    else:
                        count += 1
                        min_idx = dic[next][list_i]
                        next = A[min_idx] + diff
                res = max(res, count)
        return res
                    
                    
