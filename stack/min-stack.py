class MinStack:

    def __init__(self):
        self.stack = []
        self.min_elm = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_elm = min(self.min_elm, val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_elm = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_elm
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()