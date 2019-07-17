class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Method 1:
        
        #if len(s) == 1:
        #    return int(s)
        #res, num, symbol = 0, 0, ''
        #stack = []
        #stack.append(1)
        #for char in s:
        #    if char.isdigit():
        #        num = num * 10 + int(char)
        #    elif char == '+' or char == '-':
        #        if symbol == '*': # before is * or / 
        #            res = res * num
        #        elif symbol == '/':
        #            res = res / num
        #        else:
        #            res = num
        #        sign = 1 if char == '+' else -1
        #        stack.append(res)
        #        stack.append(sign)
        #        symbol = ''
        #        num = 0
        #        
        #    elif char == '*' or char == '/':                
        #        if symbol == '*':  # before is * or / 
        #            res = res * num
        #        elif symbol == '/':
        #            res = res / num
        #        else:
        #            res = num
        #        symbol = char
        #        num = 0
        #
        #if symbol == '*':
        #    res = res * num
        #elif symbol == '/':
        #    res = res / num
        #else:
        #    res = num
        #if stack:
        #    res *= stack.pop()
        #while stack:
        #    temp = stack.pop()
        #    temp *= stack.pop()
        #    res += temp
        #
        #return res
        
        # Method 2:
        stack = []
        pre_op = '+'
        num = 0
        
        for i, char in enumerate(s):
            if char.isdigit():
                num =  num * 10 + int(char)
            if i == len(s) -1 or char in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    prenum = stack.pop()
                    if num *  prenum < 0:
                        stack.append(-(prenum*-1/num))
                    else:
                        stack.append(prenum/num)
                pre_op = char
                num = 0
        return sum(stack)
                        
            
            
            
            
            
            
            
