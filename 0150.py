class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Method 1
        # stack = []
        # for c in tokens:
        #     if c not in '+-*/':
        #         stack.append(c)
        #     else:
        #         b0 = stack.pop()
        #         a0 = stack.pop()
        #         
        #         a = int(a0)
        #         b = int(b0)
        #         if c == '+':
        #             c_ = a + b
        #         elif c == '-':
        #             c_ = a - b
        #         elif c == '*':
        #             c_ = a * b
        #         elif c == '/':
        #             if a*b < 0:
        #                 c_ = -int(-a/b)
        #             else:
        #                 c_ = int(a / b)
        #         stack.append(c_)
        # return stack.pop()
    
        # Method 2
        stack = []
        for c in tokens:
            if c not in '+-*/':
                stack.append(c)
            else:
                b = stack.pop()
                a = stack.pop()
                
                if c == '/' and int(a) * int(b) < 0:
                    c_ = -int(-int(a)/int(b))
                else:
                    c_ = eval(a + c + b)
            
                stack.append(str(c_))
        return int(stack.pop())
                    
