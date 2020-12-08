from collections import deque


class MovingAverageFromDataStream:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.size = size

    def next(self, val: int) -> float:
        n = len(self.queue)
        if n >= self.size:
            self.queue.popleft()
            self.queue.append(val)
        else:
            self.queue.append(val)
        return sum(self.queue) / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
