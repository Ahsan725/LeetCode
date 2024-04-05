class Solution:
    def reverseParentheses(self, s: str) -> str:
        inputString = s
        stack = []
        result = ""
    
        for char in inputString:
            if char == '(':
                stack.append(result)
                result = ""
            elif char == ')':
                result = stack.pop() + result[::-1]
            else:
                result += char
            
        return result