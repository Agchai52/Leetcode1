class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        '''
        1. endWord not in wordList
        2. all distance from beginWord to word in wordlist > 1
        3. func: word distance 
        4. build a graph according to worddistance (indegree)
        5. oneDegree
        '''
        # Method BFS O(NL)
        if endWord not in wordList: return 0
        wordset = set(wordList)
        queue = collections.deque()
        queue.append((beginWord, 1))
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in xrange(len(word)):
                for c in 'abcdefghigklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    newword = word[:i] + c + word[i+1:]
                    if newword in wordset and newword != word:
                        wordset.remove(newword)
                        queue.append((newword, length+1))
        return 0
            
            
        
