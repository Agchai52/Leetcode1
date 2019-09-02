class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Method 1:
        '''
        1. ' ': s.strip() delete space
        2. 'e': digit + e + '+/-'+ integer
        3. sign: digit + e + '+/-'+ integer 
        4. '.': only once before e
        '''
        s = s.strip() 
        if not s: return False
        
        isDot, isDigit, isE = False, False, False
        # isdecimal
        for i, x in enumerate(s):
            if x == 'e':
                if not isDigit or isE:
                    return False
                isE = True
                isDigit = False
            elif x in '+-':
                if i != 0 and s[i-1]!= 'e':
                    return False
            elif x == '.':
                if isDot or isE:
                    return False
                isDot = True
            elif x.isdecimal():
                isDigit = True
            else: return False
        return isDigit
        
        # Method 2: DFA https://www.cnblogs.com/zuoyuan/p/3703075.html
        '''
        INVALID=0; SPACE=1; SIGN=2; DIGIT=3; DOT=4; EXPONENT=5;
        #0invalid,1space,2sign,3digit,4dot,5exponent,6num_inputs
        transitionTable=[[-1,  0,  3,  1,  2, -1],    #0 no input or just spaces 
                         [-1,  8, -1,  1,  4,  5],    #1 input is digits 
                         [-1, -1, -1,  4, -1, -1],    #2 no digits in front just Dot 
                         [-1, -1, -1,  1,  2, -1],    #3 sign 
                         [-1,  8, -1,  4, -1,  5],    #4 digits and dot in front 
                         [-1, -1,  6,  7, -1, -1],    #5 input 'e' or 'E' 
                         [-1, -1, -1,  7, -1, -1],    #6 after 'e' input sign 
                         [-1,  8, -1,  7, -1, -1],    #7 after 'e' input digits 
                         [-1,  8, -1, -1, -1, -1]]    #8 after valid input input space
        state=0; i=0
        while i<len(s):
            inputtype = INVALID
            if s[i]==' ': inputtype=SPACE
            elif s[i]=='-' or s[i]=='+': inputtype=SIGN
            elif s[i] in '0123456789': inputtype=DIGIT
            elif s[i]=='.': inputtype=DOT
            elif s[i]=='e' or s[i]=='E': inputtype=EXPONENT
            
            state=transitionTable[state][inputtype]
            if state==-1: return False
            else: i+=1
        return state == 1 or state == 4 or state == 7 or state == 8
        '''
                
