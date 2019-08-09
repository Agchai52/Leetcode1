class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        dictionary = {'2':'abc','3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        self.dfs(dictionary, 0, res, '', digits)
        return res
    
    def dfs(self, dic, index, res, path, string):
        if index == len(string):
            res.append(path)
            return
        for i in dic[string[index]]:
            self.dfs(dic, index+1, res, path+i, string)
            
