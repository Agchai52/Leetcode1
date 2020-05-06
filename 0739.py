class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        """
              0,  1,  2,  3,  4,  5,  6,  7
        T = [73, 74, 75, 71, 69, 72, 76, 73]
                                          i
                                         cur 
        stack = [6]
        res[cur] = i - cur
        res = [1, 1, 4, 2, 1, 1, 0, 0]
        """
        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res
