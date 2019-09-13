class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # https://github.com/shiyanhui/Algorithm/blob/master/LeetCode/Python/291%20Word%20Pattern%20II.py
        if not pattern and not str: return True
        if not pattern or not str: return False
        r1, r2 = {}, {}
        return self.match(pattern, str, r1, r2)
    
    def match(self, pattern, str, r1, r2):
        if not pattern and not str:
            return True

        if not pattern and str or pattern and not str:
            return False

        char = pattern[0]
        for j in xrange(len(str)):
            substr = str[:j + 1]
            if char not in r1 and substr not in r2:
                r1[char] = substr
                r2[substr] = char

                if self.match(pattern[1:], str[j + 1:], r1, r2):
                    return True

                del r1[char]
                del r2[substr]

            elif (char in r1 and r1[char] == substr and
                    self.match(pattern[1:], str[j + 1:], r1, r2)):
                return True

        return False
        
