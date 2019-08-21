class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Method 1: Iteration
        #lv1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten \
        #       Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        #lv2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        #lv3 = "Hundred"
        #lv4 = "Thousand Million Billion".split()
        #words, digit = [], 0
        #while num:
        #    token, num = num % 1000, num / 1000
        #    char = ''
        #    if token > 99:
        #        char = lv1[token/100] + ' ' + lv3 + ' '
        #        token %= 100
        #    if token > 19:
        #        char += lv2[token/10-2] + ' '
        #        token %= 10
        #    if token > 0:
        #        char += lv1[token] + ' '
        #    char = char.strip() # remove leading whitespace
        #    if char:
        #        char += ' ' + lv4[digit-1] if digit >= 1 else ''
        #        words.append(char)
        #    digit += 1
        #return ' '.join(words[::-1]) or 'Zero'
        
        # Method 2: Recursion
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n/10-2]] + words(n%10)
            if n < 1000:
                return [to19[n/100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand','Million','Billion'),1): # p start from 1
                if n < 1000 ** (p+1):
                    return words(n/1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'
                
            
