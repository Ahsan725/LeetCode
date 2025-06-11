class Solution:
    def isValid(self, s: str) -> bool:
        #if it begisn with an open false
        #if there is more opens than close or more close then open-> false
        #count of open drops before count of close does -> false
        stack = []
        paramap = {")": "(", "]": "[", "}": "{"}
        open_count = 0
        
        for c in s:
            if c in "({[":
                #open para
                stack.append(c)
                open_count += 1 
            
            if c in ")}]":
                if open_count > 0:
                    if stack and stack[-1] == paramap[c]:
                        stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
                
                