class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = '1'
        
        for i in xrange(n-1):
            count = 1
            digit = say[0]
            old_say = say
            say = ''
            for c in old_say[1:]:
                if c == digit:
                    count = count + 1
                else:
                    say = say + str(count) + digit
                    digit = c
                    count = 1
            say = say + str(count) + digit
        return say
                
