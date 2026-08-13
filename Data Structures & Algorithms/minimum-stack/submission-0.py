class MinStack:

    def __init__(self):
        self.miniStack = deque()
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.miniStack.append(val)
        if self.minVal > val:
            self.minVal = val

    def pop(self) -> None:
        popped = self.miniStack.pop()
        if popped == self.minVal:
            if self.miniStack:
                self.minVal = min(self.miniStack)
            else:
                self.minVal = float('inf')

    def top(self) -> int:
        return self.miniStack[-1]

    def getMin(self) -> int:
        return self.minVal
