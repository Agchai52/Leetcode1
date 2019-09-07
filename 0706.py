class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10
        self.m = [None] * self.size
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size
        
        if self.m[index] == None:
            self.m[index] = ListNode(key, value)
        else:
            curNode = self.m[index]
            while True:
                if curNode.key == key:
                    curNode.val = value
                    return
                if curNode.next == None:
                    break
                curNode = curNode.next
            curNode.next = ListNode(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.size
        if self.m[index] == None:
            return -1
        else:
            curNode = self.m[index]
            while curNode:
                if curNode.key == key:
                    return curNode.val
                curNode = curNode.next
            return -1
        
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.size
        if self.m[index] == None:
            return
        elif self.m[index] != None:
            tempHead = self.m[index]
            if tempHead.key == key:
                self.m[index] = tempHead.next
            else:
                preHead, curHead = tempHead, tempHead.next
                while curHead:
                    if curHead.key == key:
                        preHead.next = curHead.next
                        break
                    curHead = curHead.next
                    preHead = preHead.next
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
