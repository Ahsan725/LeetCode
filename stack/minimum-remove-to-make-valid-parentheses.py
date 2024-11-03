class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # res = []
        # count = 0

        # for c in s:
        #     if c == '(':
        #         res.append(c)
        #         count += 1
        #     elif c == ')' and count > 0:
        #         res.append(c)
        #         count -= 1
        #     elif c != ')':
        #         res.append(c)
        # result = []
        # for c in res[::-1]:
        #     if c == '(' and count > 0:
        #         count -= 1
        #     else:
        #         result.append(c)
        # return "".join(result[::-1])
        #below is the stack solution which will be eaasier to talk about 
        stack = []
        to_remove = set()

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        to_remove.update(stack)
        res = []
        for i, c in enumerate(s):
            if i not in to_remove:
                res.append(c)
        return "".join(res)

