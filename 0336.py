class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        '''
        input: ["bat","tab","cat"] or ['ls', 'ssl'] or ['wow', '']
        output: [[0,1], [1,0]]
        Method 1: Brute Force
        0. words unique? distinct indices?
        1. 2Cn, 'battab' and 'tabbat'
        2. isPralindrome
        3. res.append  
        Method 2: HashTable
        1. table = {words[i][::-1]: i}
        2. words[i] is valid, requirs ''
        3. words[j] in table, res.append([i,j], [j,i])
        3. 
        
        '''
        '''
        # Method 1: TLE Time = O(n^2k)
        if len(words) <= 1: return []
        n = len(words) # n = 3
        res = []
        
        def isValid(s):
            # return s == s[::-1]
            m = len(s) # 6, s = 'tabcat'
            for i in xrange(m/2): # [0,1,2] 
                if s[i] != s[m-i-1]: # i = 2 , m -i -1 = 3
                    return False
            return True
        
        
        for i in range(n-1): # [0,1] i = 1
            for j in range(i+1, n): # [1,2] j = 2
                if isValid(words[i] + words[j]): # words[i] = 'tab', word[j]        = 'cat'
                    res.append([i,j]) # res = [[0,1]]
                if isValid(words[j] + words[i]): # 
                    res.append([j,i]) # res = [[0,1], [1,0]]
        return res

        '''
        # Method 2: Hash Table
        if len(words) <= 1: return []
        n = len(words) # n = 3
        res = set()
        table = dict()
        
        def isValid(s):
            # return s == s[::-1]
            m = len(s) 
            for i in xrange(m/2): 
                if s[i] != s[m-i-1]:
                    return False
            return True
        
        for i, w in enumerate(words):
            table[w[::-1]] = i
        for i, w in enumerate(words):
            if isValid(w) and '' in table and w != '':
                res.add((i,table['']))
                res.add((table[''], i))
            if w in table and i != table[w]:
                res.add((i, table[w]))
                res.add((table[w], i))
            
            for x in xrange(1,len(w)):
                left, right = w[:x], w[x:]
                if isValid(left) and right in table:
                    res.add((table[right], i))
                if isValid(right) and left in table:
                    res.add((i, table[left]))
        return list(res)
                
            
