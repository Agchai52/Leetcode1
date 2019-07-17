class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return int(s)
        
        stack = []
        res, num, sign = 0, 0, 1
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == '+' or char == '-':
                res = res + sign * num
                sign = 1 if char == "+" else -1
                num = 0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif char == ')':
                res = res + sign * num
                sign = stack.pop()
                preres = stack.pop()
                res = preres + sign * res
                num, sign = 0, 1
        res = res + sign * num
        return res
            
                
                    
