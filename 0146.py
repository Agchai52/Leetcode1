class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict() # self.cache: {key : value}
        self.visited = []
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        self.visited.remove(key)
        self.visited.append(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key not in self.cache:
            if len(self.visited) == self.capacity:
                least = self.visited.pop(0)
                del self.cache[least]
            
        else:
            self.visited.remove(key)
        self.cache[key] = value
        self.visited.append(key)   

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
