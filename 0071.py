class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Method 1: Slow
        #string, stack = '', []
        #i = 1
        #while i < len(path):
        #    if path[i] != '/':
        #        string = string + path[i]
        #        if ( i < len(path)-1 and path[i+1] == '/' ) or ( i==len(path)-1 and string != '' ): 
        #            if string == '..':
        #                if stack:
        #                    stack.pop()                       
        #                string = ''
        #            elif string == '.':
        #                string = ''
        #            else:
        #                stack.append(string)
        #                string = ''
        #            
        #    i += 1
        #
        #cpath = ''
        #if stack:
        #    while stack:
        #        cpath = cpath + '/' + stack.pop(0) 
        #else:
        #    cpath = '/'
        #
        #return cpath
        
        # Method 2
        stack = []
        dirs = path.split('/')
        for d in dirs:
            if d == '.' or not d:
                continue
            if d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return '/' + '/'.join(stack)
                
            
