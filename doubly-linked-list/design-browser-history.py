class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        # Remove forward history and add new URL
        self.stack = self.stack[:self.i + 1]
        self.stack.append(url)
        self.i += 1

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