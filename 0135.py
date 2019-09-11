class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        '''
        1st idea, scan multiple times untill 2 conditions satisfied
        but not efficient, time O(N^N)
        2nd idea, save effect, e.g. for ratings[i] save j effected by i.
        and save it in table, until que empty
        1. hash table save effected
        2. bfs to explore 
        '''
        
        '''
        # Method 1: BFS TLE
        if not ratings: return 0
        if len(ratings) == 1: return 1
        
        def isEffect(i, j):
            if ratings[j] > ratings[i]:
                return True
            else:
                return False
        n = len(ratings)
        res = [1] * n
        que = collections.deque()
        effect = collections.defaultdict(list)
        for i in range(n):
            if i == 0:
                if isEffect(i, i+1):
                    effect[i].append(i+1)
                    que.append(i+1)
            elif i == len(ratings)-1:
                if isEffect(i, i-1):
                    effect[i].append(i-1)
                    que.append(i-1)
            else:
                if isEffect(i, i-1):
                    effect[i].append(i-1)
                    que.append(i-1)
                if isEffect(i, i+1):
                    effect[i].append(i+1)
                    que.append(i+1)                
        
        #print(effect)
        #print(que)
        #print(res)
        while que:
            j = que.popleft()
            if 0<j<n and res[j]>res[j-1] and res[j]>res[j+1]: # avoid counting Summit twice
                continue
            res[j] += 1
            if j not in effect:
                continue
            for i in effect[j]:
                que.append(i)
            #print(que)
            #print(res)
    
        return sum(res)
        '''
        
        # Method: scan from left to right then scarn from right to left, store max 
        
        if not ratings: return 0
        if len(ratings) == 1: return 1
        
        n = len(ratings)
        res = [1] * n
        # Scan1 left to right
        for i in range(1, n):
            if ratings[i-1] < ratings[i] and res[i-1] >= res[i]:
                res[i] = res[i-1] + 1
        
        # Scan2 right to left:
        for i in range(0, n-1)[::-1]:
            if ratings[i+1] < ratings[i] and res[i+1] >= res[i]:
                res[i] = max(res[i], res[i+1]+1)
                
        return sum(res)
            
        
