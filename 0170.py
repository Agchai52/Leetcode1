class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.map[number] = self.map.get(number, 0) + 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.map:
            if value-n in self.map:
                if value-n != n or value-n == n and self.map[n] > 1:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
