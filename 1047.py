class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(S):
            if not stack:
                stack.append(S[i])
            elif S[i] == stack[-1]:
                stack.pop()
            elif S[i] != stack[-1]:
                stack.append(S[i])
            i += 1
        return ''.join(stack)
        
