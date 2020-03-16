class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if not list1 or not list2: return []
        min_sum = len(list1) + len(list2)
        min_word = []
        table1 = dict()
        
        for i in range(len(list1)):
            if list1[i] not in table1:
                table1[list1[i]] = i
        
        for i in range(len(list2)):
            word = list2[i]
            if word in table1:
                if table1[word] + i < min_sum:
                    min_sum = table1[word] + i
                    min_word = [word]
                elif table1[word] + i == min_sum:
                    min_word.append(word)
       
        return min_word
