class Solution(object):
    def lengthLongestPath(self, inputs):
        """
        :type input: str
        :rtype: int
        """
        if not input:
            return 0
        string = inputs.split('\n')
        stack = [(-1, 0)] # cur_depth, cur_len
        
        max_len = 0
        for s in string:
            depth = s.count('\t')
            s = s.replace('\t','')
            while stack and depth <= stack[-1][0]:
                stack.pop()
            if '.' not in s: # directory
                stack.append((depth, len(s) + stack[-1][1] + 1))
            else: # file
                max_len = max(max_len, len(s) + stack[-1][1])
        
        
        return max_len
