class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.min:
            self.min.append(x)
        else:
            y = self.min[-1]
            if x <= y:
                self.min.append(x)
            else:
                self.min.append(y)

    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()