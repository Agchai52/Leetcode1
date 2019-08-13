class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.match(self.root, word, 0)
        
    
    def match(self, current, word, index):
        if current == None:
            return False
        if index == len(word):
            return current.isword
        if word[index] != '.':
            return current != None and self.match(current.children.get(word[index]), word, index+1)
        else:
            for child in current.children.values():
                if self.match(child, word, index+1):
                    return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
