from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        # Recursive function to build valid parentheses combinations
        # strsofar: current parentheses string being built
        # numofopen: number of '(' used so far
        # numofclose: number of ')' used so far
        def addparen(strsofar: str, numofopen: int, numofclose: int):
            # Base case: if the current string has 2 * n characters, it's complete
            if len(strsofar) == 2 * n:
                self.res.append(strsofar)
                return

            # If we can still add an open parenthesis, do it
            if numofopen < n:
                addparen(strsofar + '(', numofopen + 1, numofclose)

            # Only add a close parenthesis if there are unmatched opens
            if numofclose < numofopen:
                addparen(strsofar + ')', numofopen, numofclose + 1)

        # Start with an empty string and zero open/close parentheses used
        addparen('', 0, 0)
        return self.res
