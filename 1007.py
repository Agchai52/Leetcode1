class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        '''
        Method 1: 2 Hash Tables Time = O(2*N+K*N) = O(N), Space = O(6*2)=O(1)
        1. mapA = {val: num}
        2. mapB = {val: num}
        3. for each val in mapA, check if len(A)-num in mapB, main min(len(A)-num)
        4. for each val in mapB, check if len(A)-num in mapA, main min(len(A)-num)
        Method 2: Time = O(2*N+K*N) = O(N), Space = O(K*2) = O(1)
        1.
        2.
        3. check 1-6 in both A and B
        
       
        '''
        
        '''
        if len(A) <= 1: return 0
        mapA = collections.Counter(A)
        mapB = collections.Counter(B)
        res = float('inf')
        if len(mapA.values()) == 1 or len(mapA.values()) == 1: return 0
        flag = True
        for x in range(1,7):
            if x not in mapA and x not in mapB:
                continue
            if x in mapA and x in mapB:
                if mapA[x] + mapB[x] < len(A):
                    continue
                else:
                    for i in range(len(A)):
                        if A[i] != x and B[i] != x:
                            flag = False
                            break
                    if flag:
                        fre_A = len(A) - mapA[x]
                        fre_B = len(B) - mapB[x]
                        res = min(res, fre_A, fre_B)
  
        
        return res if res != float('inf') else -1
        '''
        
        if len(A) <= 1: return 0
        mapA = collections.defaultdict(list) 
        mapB = collections.defaultdict(list)       
                
        res = float('inf')
        
        for i in xrange(len(A)):
            mapA[A[i]].append(i)
            mapB[B[i]].append(i)
                        
        if len(mapA.values()) == 1 or len(mapA.values()) == 1: return 0
            
        for v in mapA:
            if v not in mapB: 
                continue
            if len(set(mapA[v])|set(mapB[v])) < len(A):
                continue
            fre_A = len(A) - len(mapA[v])
            fre_B = len(B) - len(mapB[v])
            res = min(res, fre_A, fre_B)
        return res if res != float('inf') else -1
        
       
                
                   
