class Solution(object):
    def toGoatLatin(self, s):
        """
        :type S: str
        :rtype: str
        """
        '''
        0. string to list
        1. s[i][0] in 'aeiouAEIOU', s += s[i][1:]+s[0]
        2. s[i][0] not in, s += s.pop(0) + 'ma'
        3. i s[i] += (i+1) * a
        4. list to string
        '''
        if not s: return ''
        res = []
        string = s.split(' ')
        
        for i, word in enumerate(string):
            if word[0] in 'aeiouAEIOU':
                new = word 
            else:
                new = word[1:] + word[0]
            new += 'ma' + 'a'*(i+1)
            res.append(new)
        return ' '.join(res)
        
