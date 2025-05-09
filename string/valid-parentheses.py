class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []

        #edge cases
        #input too small
        if len(s) < 2:
            return False

        for c in s:
            if c in ")}]":
                #we found a closing parenthesis 
                if pairs[c] != stack[-1]:
                    #we did not find correct matching
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True 