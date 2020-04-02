class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.code = collections.defaultdict(set)
        for s in dictionary:
            s_abb = self.encode(s)
            self.code[s_abb].add(s)    
    
    def encode(self, s):
        if not s:
            return ""
        return s[0] + str(len(s)-2) + s[-1]
        
        
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        s_abb = self.encode(word)
        return s_abb not in self.code or len(self.code[s_abb])==1 and word in self.code[s_abb]
        
