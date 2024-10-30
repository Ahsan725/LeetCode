class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        prev_operator = "+"
        curr_num = 0

        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = (curr_num * 10) + int(s[i])
            
            if s[i] in "+-/*" or i == len(s) -1:
                if prev_operator == '+':
                    stack.append(curr_num)
                if prev_operator == '-':
                    stack.append(-curr_num)
                if prev_operator == '*':
                    stack[-1] = stack[-1] * curr_num
                if prev_operator == "/":
                    stack[-1] = int(stack[-1] / curr_num)
                
                prev_operator = s[i]
                curr_num = 0

        return sum(stack)
        
        