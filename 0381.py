import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.dict[val] = 1
            self.list.append(val)
            return True
        else:
            self.dict[val] += 1
            self.list.append(val)
            return False
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            if self.dict[val] > 1:
                self.dict[val] -= 1
            else:
                del self.dict[val]
            self.list.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        i = random.randrange(0, len(self.list))
        return self.list[i]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
