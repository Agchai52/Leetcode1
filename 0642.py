class TrieNode(object):
    
    def __init__(self):
        self.children = dict()
        self.sentence = set()

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.buff = ''
        self.stimes = collections.defaultdict(int)
        self.trie = TrieNode()
        
        for s, t in zip(sentences, times):
            self.stimes[s] = t
            self.addSentence(s)
        
        self.tnode = self.trie

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        ans = []
        if c != '#':
            self.buff += c
            if self.tnode:
                self.tnode = self.tnode.children.get(c)
            if self.tnode:
                ans = sorted(self.tnode.sentence, key = lambda x: (-self.stimes[x], x))[:3]
        else:
            self.stimes[self.buff] += 1
            self.addSentence(self.buff)
            self.buff = ''
            self.tnode = self.trie
        return ans
        
    def addSentence(self, s):
        node = self.trie
        for char in s:
            child = node.children.get(char)
            if child is None:
                child = TrieNode()
                node.children[char] = child
            node = child
            node.sentence.add(s)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
