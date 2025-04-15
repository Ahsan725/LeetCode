class Solution:
    def decodeString(self, s: str) -> str:
        #we will use a stack and also use the same stack to store the res
        #keep adding to the stack until we get to a closed bracket
        #do not add closed brack but start popping until the opening bracket is popped off
        #after this there will be a number (could be more than one digit)
        #get the number and all the digits in the right order as string -> then convert it into a num 
        #after that add the subtring back onto the stack * k times and carry on
        
        stack = []
        
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() #for the opening bracket to fall off
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.extend(int(num) * substr)
        return "".join(stack)