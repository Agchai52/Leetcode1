class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        i = 0
        magazine = list(magazine)
        ransomeNote = list(ransomNote)
        for c in ransomeNote:
            if c in string.lowercase:
                if c not in magazine:
                    return False
                else:
                    i += 1
                    magazine.remove(c)
                
        if i == len(ransomNote):
            return True
        else:
            return False
        
