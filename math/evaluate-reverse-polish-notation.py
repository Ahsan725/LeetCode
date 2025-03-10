from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if stack and token in {"+", "-", "*", "/"}:
                second = stack.pop()
                first = stack.pop()
                
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    # Division should truncate towards zero
                    stack.append(int(first / second))
            else:
                stack.append(int(token))  # Convert operand to int and push to stack

        return stack.pop()  # Final result
