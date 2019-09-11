class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # Method: cannot DFS(MLE), has to BFS
        '''
        # Method: TLE
        if endWord not in wordList: return []
        self.minL = float('inf')
        wordset = wordList
        res = []
        oneDiff = collections.defaultdict(list)
        
        que = collections.deque()
        que.append(beginWord)
        
        def dfs(path, word, endWord):
            #print(path)
            if word == endWord:
                if path not in res:
                    self.minL = min(self.minL, len(path))
                    res.append(path)
                return
            if not oneDiff[word]:
                return
            temp = []
            while oneDiff[word]:
                nextWord = oneDiff[word].pop()
                temp.append(nextWord)
                #print(word, nextWord)
                #print('==')
                dfs(path+[nextWord], nextWord, endWord)
            oneDiff[word] = temp   
            path.pop(0)
        
        
        flag = False
        while que:
            word = que.popleft()
            if word == endWord:
                flag = True
                continue
            
            for i in range(len(word)):
                for c in 'abcdefghigklmnopqrstuvwxyz':
                    if word[i] == c:
                        continue
                    new = word[:i] + c + word[i+1:]
                    if new in wordList and new not in oneDiff:
                        oneDiff[word].append(new)                        
                        que.append(new)
        #print(oneDiff)    
        if not flag: return []
        dfs([beginWord], beginWord, endWord)
        i = 0
        while i < len(res):
            if len(res[i]) > self.minL:
                del res[i]
                continue
            i += 1
        
        return res
    
        '''
        # Method https://blog.csdn.net/qian2729/article/details/50576161
        wordlist=set(wordList)
        res= []
        layer = {}
        layer[beginWord] = [[beginWord]]
        
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            newword=w[:i] + c + w[i+1:]
                            if newword in wordlist:
                                newlayer[newword] += [j+[newword] for j in layer[w]]
            wordlist -=set(newlayer.keys())
            layer = newlayer
            
        return res
