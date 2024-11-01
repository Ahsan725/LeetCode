class Solution:
    def simplifyPath(self, path: str) -> str:
        #Working on the canonical path basically means modifying the input string in these conditopns:
        #path = "/home/"
        #a stack may or may not be useful 
        #approach -> use a stack to view the last directory etc to adjust the final path
        #also thinking of spliting using "/" a delimitter 
        stack = ["/"]
        dir_list = path.split("/") #    ['', 'path', 'etc', 'passwd']
        # res = ["/"]

        #sample input = "/home/user/Documents/../Pictures"
        for directory in dir_list:
            if directory:
                if directory == "..": #This means go back to the parent directory 
                    stack.pop() #popped back to parent directory
                    if len(stack) >= 2:
                        stack.pop()
                    continue #skip adding the ".."
                elif directory == ".": #handles the case of current directory
                    continue
                stack.append(directory)
                stack.append("/")
        if len(stack) > 1:
            stack.pop()
        #adds just a slash incase of an empty path name 
        if len(stack) <= 0:
            stack.insert(0, "/")
        

        final_str = "".join(stack)
        return final_str



        #the path must start with a single /

        #Directories must be serperated by only one slash

        #The path must not end with a slash unless it is root 

        #the path must not have any single or double periods -> convert them by going back one directory for ".."
        #and ignoring "."
        