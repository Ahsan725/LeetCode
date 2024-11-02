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
        close_to_open ={"}":"{", "]":"[", ")":"("}

        for char in s:
            if char in close_to_open: #this just means that it is a closing bracket
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop() #basicaly means it closed one of the brackets
                else:
                    return False
            else:
                stack.append(char)
            
        return True if not stack else False

