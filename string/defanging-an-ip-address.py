class Solution:
    def defangIPaddr(self, address: str) -> str:
        #seperate the tokens and split on "."

        res = []

        for c in address:
            if c == ".":
                res.append("[.]")
            else:
                res.append(c)
        
        final_res = "".join(res)
        return final_res

        