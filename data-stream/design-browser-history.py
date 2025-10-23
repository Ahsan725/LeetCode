class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.i = 0
        self.len = 1

    def visit(self, url: str) -> None:
        #do we have enough indices ti add
        if len(self.stack) < self.i + 2:
            self.stack.append(url)
        else:
            self.stack[self.i + 1] = url
        self.i += 1 #increment the index
        self.len = self.i + 1 #increment the len variable 

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.stack[self.i]
        
    def forward(self, steps: int) -> str:
        self.i = min(len(self.stack) - 1, self.i + steps)
        return self.stack[self.i]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)