#  https://leetcode.com/problems/lru-cache/solution/
# optimal solution uses a double linked list to maintain the cache
# you store the pointer to the node in a hash map
# delete the node in O(1) and insert it again in O(1)
# put is easy

from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.time = 0
        self.cache = {} #dafaultdict(lambda: {"value" : -1, "time" : 0})
        self.keyQueue = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.cache:
            self.cache[key]["time"] = self.time
            self.keyQueue.append((key,self.time))
            return self.cache[key]["value"]

        return -1

    def myDeque(self) -> None:
        while self.keyQueue:
            key, time = self.keyQueue.popleft()
            if time == self.cache[key]["time"]:
                del self.cache[key]
                return

    def put(self, key: int, value: int) -> None:
        existingValue = self.get(key)
        if existingValue == -1:
            if len(self.cache) >= self.capacity:
                self.myDeque()
            self.keyQueue.append((key,self.time))
            self.cache[key] = {
                "value" : value,
                "time" : self.time
            }

        else:
            self.cache[key]["value"] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
