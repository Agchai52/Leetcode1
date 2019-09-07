class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)


        
   
        

    def pop(self):
        """
        :rtype: int
        """
        
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.stack)

    def popMax(self):
        """
        :rtype: int
        """
        
        x = self.peekMax()
        for i, v in enumerate(self.stack[::-1]):
            if v == x:
                break
        n = len(self.stack)
        del self.stack[n-i-1]
        return x


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
