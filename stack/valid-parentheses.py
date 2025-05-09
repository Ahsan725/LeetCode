class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in ")}]":
                #we found a closing parenthesis 
                if not stack or pairs[c] != stack[-1]:
                    #we did not find correct matching or found a closing paren before an opening 
                    return False
                else:
                    if stack:
                        stack.pop()
            else:
                stack.append(c)
        if stack: #if stack has some elements that means we did not find enough openings 
            return False
        else:
            return True 