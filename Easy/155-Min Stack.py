# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.nextMin = defaultdict(list)
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min is None:
            self.min = val
        elif self.min == val:
            self.nextMin[val].append(val)
        elif self.min > val:
            self.nextMin[val] = [self.min]
            self.min = val
        #print(self.stack,self.min)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min:
            if self.stack and self.nextMin[val]:
                self.min = self.nextMin[val].pop()
            else:
                self.min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
