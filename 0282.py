class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # Method: backtracking
        if not num: return []
        if len(num) == 1: return int(num[0]) == target
        if abs(target) > 10:
            if int(num) == target: return [num]
            elif -int(num) == target: return []
        res = []
        pre_o = '' if num[0] != '0' else '+'
        self.dfs(num, 1, num[0], target, res, pre_o)
        return res
    
    def dfs(self, num, index, path, target, res, pre_o):
        if index == len(num):
            if eval(path) == target:
                res.append(path)
            return
        
        for o in ['','+','-','*']:            
            # Deal with zeros: not valid: +05, -00, *0000
            if o == '' and num[index-1] == '0' and pre_o != '' :
                continue
            pre_o = o            
            self.dfs(num, index+1, path+o+num[index], target, res, pre_o)
            
        
            
        
