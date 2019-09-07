class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # Method 1: Hash Table
        # https://blog.csdn.net/fuxuemingzhu/article/details/79183289
        if len(chars) <= 1: return len(chars)
        pre = chars[0]
        count = 0
        pos = 0
        for ch in chars:
            if pre == ch:
                count += 1
            else:
                chars[pos] = pre
                pos += 1
                if count > 1:
                    count = str(count)
                    for i in range(len(count)):
                        chars[pos] = count[i]
                        pos += 1
                count = 1
                pre = ch
        chars[pos] = pre
        pos += 1
        if count > 1:
            count = str(count)
            for i in range(len(count)):
                chars[pos] = count[i]
                pos += 1
        return pos


        
           
                
            
            
                
        
                    
                     
        
