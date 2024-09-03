class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #initialize the stack 
        for char in s: #go through character in the string s 
            if char in '({[': # check if they belong to the opening brackets
                stack.append(char) #if they do add them to the stack at the end 
            else: # if they are closing brackets
                if not stack: #if we have never encontered an opening bracket which would mean it could never be valid
                    return False #so we return false immediately
                top = stack.pop() #if we have seen an opening bracket, pop it which basically means examine it 
                if (char == ')' and top != '(') or \
                   (char == '}' and top != '{') or \
                   (char == ']' and top != '['): #if the character is opening & it NOT matches with its kind of closing
                    return False #return false
        return not stack #if everything has been matched up it will empty the stack and not return false at any point which means we can just return true if stack is empty or false if it is not. 
