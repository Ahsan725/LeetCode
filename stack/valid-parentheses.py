class Solution:
    def isValid(self, s: str) -> bool:
        #I am thinking of using a stack because of the nature f the problem. Where we are going back to look at the
        #last added element or bracket in this case. And see if that is closing the current one 

        #stack = []
        # "({[" add this to the stack and then we will check when we encounter the first closng para

        #([{]}) -> stack =["(", "[", "{", ""]
        #stack.pop() -> 

        #if not stack:
        #return True
        #else False

        stack = []

        if len(s) <=1 or len(s) % 2 != 0:
            return False

        for char in s:
            if char in "({[":
                stack.append(char)
            if char in ")]}" and stack:
                if char == ')' and stack[-1] == "(":
                    stack.pop()
                if char == '}' and stack[-1] == "{":
                    stack.pop()
                if char == ']' and stack[-1] == "[":
                    stack.pop()
        
        if not stack:
            return True
        else:
            return False
