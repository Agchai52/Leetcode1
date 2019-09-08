class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        '''
        0. str to list
        1. fre of words: use hash table to count fre of words
        2. banned list: check if most fre in banned, if not delet most checke next
        3. '.,?:;'
        '''
        if not paragraph: return ''
        par = paragraph
        for c in "!,.?/;:[]{}()'":
            par = par.replace(c, ' ')
        par = par.lower().strip()
        par = par.split(' ')
        fmap = {}
        max_fre = 0
        max_word = ''
        for w in par:
            if w in banned or w == '':
                continue
            
            if w not in fmap:
                fmap[w] = 1
            else:
                fmap[w] += 1
                
            if fmap[w] > max_fre:
                max_fre = fmap[w]
                max_word = w
        return max_word
