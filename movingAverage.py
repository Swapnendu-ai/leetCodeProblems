# https://leetcode.com/problems/moving-average-from-data-stream/submissions/

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.numbers = []


    def next(self, val: int) -> float:
        if len(self.numbers) == self.size:
            self.numbers = self.numbers[1:] + [val]
        else:
            self.numbers.append(val)
        return sum(self.numbers)/len(self.numbers)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
