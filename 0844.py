class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if not S and not T: return True
        stackS = []
        stackT = []
        
        for c in S:
            if c == "#":
                if stackS:
                    stackS.pop()
            else:
                stackS.append(c)
        
        for c in T:
            if c == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(c)
        
        return stackS == stackT
