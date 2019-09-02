import heapq
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        2763: 7263 swap largest with first
        7263: 7632 swap second lagest with second
    
        1. priority que: [(-digit, index)]
        2. check digits i from left to right and compare with j digit in ordered, detect different, swap i and j
        3. repeat digit, return last one
        '''
        def swap(i,j, string):
            string[i], string[j] = string[j], string[i]
            
        
        
        # Method 1: O(NlogN)
        # if num < 12: return num
        # string = list(str(num))       
        # max_q = sorted(string, reverse=True)
        #for (i,d) in enumerate(string):                      
        #    max_val = max_q.pop(0)
        #    if d != max_val:
        #        k = string[i+1:][::-1].index(max_val)  
        #        # return last index of max_val         
        #        j = len(string) - k -1 
        #        swap(i,j, string)
        #        return int(''.join([str(c) for c in string]))
        #return num
        
        # Method 0: Brute Force
        #A = list(str(num))
        #ans = A[:]
        #for i in range(len(A)):
        #    for j in range(1+i, len(A)):
        #        A[i], A[j] = A[j], A[i]
        #        if A > ans:
        #            print(A)
        #            print(ans)
        #            print(A>ans)
        #            ans = A[:]
        #        A[i], A[j] = A[j], A[i]
        #return int(''.join(ans))
        
        # Method 2:Greedy Hash table O(N)
        A = map(int,str(num))
        last = {x:i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in xrange(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int(''.join(map(str, A)))
        return num
