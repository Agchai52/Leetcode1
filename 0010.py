class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # Method 1: NFA
        '''
        from collections import defaultdict
        
        # A dictionary is enough to represent an NFA for the purpose of
        # solving this problem. 
        # A state is represented by a number. The possible states a state 
        # transition into is represented by the mentioned dictionary.
        # It essentially maps a two-tuple (state, input) into a set of states.
        # After this dictionary is constructed, the string is simply fed into
        # the state machine, character by character, and at the end, we can
        # determine admissibility by simply checking whether the machine is
        # in the accepting state.
        
        # Note that this is a non-deterministic finite automaton, where
        # a state can transition to more than one state upon taking a single input.
        # We can "compile" this non-deterministic machine to its deterministic counterpart,
        # however, the algorithm to do so is a niche one, and not particularly easy to code
        # during an interview, if one haven't practiced it. Rather, we are keeping
        # all of the states the NFA can possibly be in, and feed the input character to
        # all of those states. 
        
        # This scheme is efficient, because in a finite-state automaton, the "method"
        # or the input string to arrive at a particular state is not important. This
        # observation allows us to represent the possible states as a "set". In the worst case,
        # we have to process every input character to the every state in the finite automaton.
        # Since we have as much states as there are characters in the pattern string, the
        # time complexity is O(sp). 
        
        # The deterministic finite automaton reduces the complexity of the admission operation
        # to O(s), just to the length of the input string. 

        states = defaultdict(lambda: set())  # (state, input) -> next state
        
        inputs = {}  # state -> symbol
        state = 0
        
        # caret and the dollar sign allow us to ignore corner cases
        # when constructing the NFA.
        s = '^' + s + '$'
        p = '^' + p + '$'
        
        i = 0
        starchain = 0
        
        # construct the NFA
        while i < len(p):
            # in our scheme, each state accepts only one input character
            # and we need to know the input value for chaining star tokens.
            inputs[state] = p[i] 
            
            if i < len(p) - 1 and p[i+1] == '*':
                # it is a star
        
                states[state, p[i]].add(state)  # to itself
                states[state, p[i]].add(state+1)  # to next state
                
                # handles chaining star operations.
                # to implement the admission of zero characters, we allow the preceding
                # states to transition into the next state. 
                starchain += 1
                for j in range(1, starchain+1):
                    states[state-j, inputs[state-j]].add(state+1)
                
                state += 1
                i += 2
            else:
                # it is a regular character. note that '.' does not receive special
                # treatment during construction.
                states[state, p[i]].add(state + 1)
                i += 1
                starchain = 0
                state += 1
                
        # the last state is the accepting state
        accept = state
                
        # prev is the possible states the machine can be in
        # next is the states the machine transitions to in one input character.
        prev = {0}
        next = set()
        
        for char in s:
            for st in prev:
                # there is a neat trick
                # since '.' is for any character, we can consider it to be inputted
                # alongside every character. 
                next = next.union(states[st, char])
                next = next.union(states[st, '.'])

            # roll the prev-next duo
            prev = next
            next = set()
  
        # after all the input characters are consumed, if the machine could possibly be
        # in the accepting state, then the machine accepts the string.
        return accept in prev
        '''
        # Method 2: Recursion
        # Edge cases for len(p) < 2
        #if s == None or p == None: return False
        #if len(p) == 0: return len(s) == 0
        #if len(p) == 1: return len(s) == 1 and (p[0] == '.' or p[0] == s[0])
        #
        ## For len(p) > 2
        #if p[1] == '*':
        #    if self.isMatch(s, p[2:]):
        #        return True
        #    return len(s) > 0 and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p)
        #else:
        #    return len(s) > 0 and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        
        # Method 3: DP
        '''
        dp[0][0] = True
        dp[i][j] # if first i in s and first j in p match each other
        =
        d[i-1][j-1] if p[j-1] == '.' or p[j-1] == s[i-1]
        d[i][j-1] if p[j-1] == '*' and p[j-2] show once
        d[i][j-2] if p[j-1] == '*' and p[j-2] doesn't show
        d[i-1][j] if p[j-1] == '*' and p[j-2] show more than once
        '''
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2,len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  
        for i in range(1,len(s) + 1):
            for j in range(1,len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                elif p[j-1] == '.' or s[i-1] == p[j - 1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[len(s)][len(p)]

                
            
#if __name__ == '__main__':
#    '''Test Cases
#    s = 'ab' 
#    p = 'a'
#    
#    s = 'ab'
#    p = 'a.'
#    
#    s = 'aaa'
#    p = 'a*'
#    
#    s = 'abb'
#    p = 'c*a.*'
#    
#    s = 'ab'
#    p = '.*'
#    
#    s = 'aab' 
#    p = 'c*a*b'
#    '''
#    s = 'eaab' 
#    p = 'ec*a*b'
#    print(Solution().isMatch(s,p))
