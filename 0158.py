"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def __init__(self):
        self.que = []
        self.endOfFile = False
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n == 0: return 0
        res = 0
        while len(self.que) < n and not self.endOfFile:
            buff4 = ['']*4
            tmp = read4(buff4)
            if tmp < 4:
                self.endOfFile = True
            for i in xrange(tmp):
                self.que.append(buff4[i])
        
        for i in xrange(min(len(self.que), n)):
            buf[i] = self.que.pop(0)
            res += 1
        return res
            
            
