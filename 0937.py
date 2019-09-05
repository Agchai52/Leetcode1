class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        '''
        1. check ide, 
        2. is dig: digit_logs = []
        3. is let: letter_logs = []
        4. sort letter_logs: string[3] ord
        5. res = letter_logs + digit_logs
        '''
        if len(logs) <= 1: return logs
        
        digits, letters = [], []
        for s in logs:
            s_split = s.split(' ')
            if s_split[1].isalpha():
                letters.append((' '.join(s_split[1:]), s_split[0]))
            else:
                digits.append(s)
        letters.sort()
        
        return [l[1]+' '+l[0] for l in letters] + digits
    
 
        
    
    
        
