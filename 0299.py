class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret =  list(secret)
        guess = list(guess)
        A = B = 0
        
        i = 0
        while i < len(secret):
            if secret[i] == guess[i]:
                A += 1
                del secret[i]
                del guess[i]
            else:
                i += 1
        
        for l in secret:
            if l in guess:
                guess.remove(l)
                B += 1
        return str(A) + 'A' + str(B) + 'B'
