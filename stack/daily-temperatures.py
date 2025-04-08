from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # Stack will hold (temperature, index)

        for i, temp in enumerate(temperatures):
            # While current temp is greater than temp on top of the stack
            while stack and temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append((temp, i))
        
        return res
