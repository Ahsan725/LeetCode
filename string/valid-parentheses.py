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
                if stack and pairs[c] != stack[-1]:
                    #we did not find correct matching
                    return False
                else:
                    if stack:
                        stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True 