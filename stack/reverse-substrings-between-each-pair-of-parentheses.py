class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        result = ""
    
        for char in s:
            if char == '(':
                stack.append(result)
                result = ""
            elif char == ')':
                result = stack.pop() + result[::-1]
            else:
                result += char
            
        return result