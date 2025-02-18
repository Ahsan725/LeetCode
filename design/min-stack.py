class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None: 
        if self.stack:
            prevmin = self.stack[-1][1] #get the most recent element and get the 1st index (2nd value in the tuple)
        else:
            prevmin = val #if it does not exist compare current val to current val 
        min_so_far = min(prevmin, val)
        self.stack.append((val, min_so_far)) 

    def pop(self) -> None: 
        self.stack.pop()

    def top(self) -> int: 
        return self.stack[-1][0] #get the most recent entry and get the 1st field (0th field)

    def getMin(self) -> int: 
        return self.stack[-1][1]
