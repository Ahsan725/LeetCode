class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None: 
        if self.stack:
            prevmin = self.stack[-1][1]
        else:
            prevmin = val
        min_so_far = min(prevmin, val)
        self.stack.append((val, min_so_far)) 

    def pop(self) -> None: 
        self.stack.pop()

    def top(self) -> int: 
        return self.stack[-1][0]

    def getMin(self) -> int: 
        return self.stack[-1][1]
