class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n -2)

        #Time: 0(n^2)
        #Space; O(n) -> recursion stack 
        
        