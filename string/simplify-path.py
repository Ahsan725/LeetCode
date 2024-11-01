class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dir_list = path.split("/")
        
        for directory in dir_list:
            if directory == "" or directory == ".":
                continue
            elif directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
        
        final_str = "/" + "/".join(stack) #this is sooo useful
        return final_str
