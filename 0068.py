class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words or not words[0]: return []
        if maxWidth < len(words[0]): return []
        
        start = 0
        end = 0
        total_len_words = 0
        count_word = 0
        res = []
        
        def createLine(word_line, total_len_words, count_word, maxWidth):
            extra_space = maxWidth - (count_word-1) - total_len_words
            total_space = extra_space + (count_word-1)
            spaces = [0] * (count_word-1)
            i = 0
            #print(total_space, total_len_words, count_word)
            if count_word > 1:
                while total_space > 0:
                    i = i % (count_word-1)
                    spaces[i] += 1
                    total_space -= 1
                    i += 1
            else:
                spaces = [total_space]
            
            spaces.append(0)
            line = ''
            for i in xrange(len(word_line)):
                line += word_line[i] + " " * spaces[i]
            return line
                       
        for i, w in enumerate(words):            
            total_len_words += len(w)
            count_word += 1
            #print(total_len_words, count_word)
            if total_len_words + count_word - 1 > maxWidth:
                pre_len = len(w)
                total_len_words -= pre_len
                count_word -= 1
                end = i 
                word_line = words[start:end]
                line = createLine(word_line, total_len_words, count_word, maxWidth)                
                res.append(line)
                count_word = 1
                total_len_words = pre_len
                start = i
            #print(total_len_words, count_word)
            #print('===')
        
        end = len(words)
        word_line = words[start:end]
        line = ' '.join(word_line)
        extra_space = ' '* (maxWidth - len(line))
        line = line + extra_space
        res.append(line)
        return res
        
        
                
                
                
