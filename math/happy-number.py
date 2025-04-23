class Solution:
    def isHappy(self, n: int) -> bool:
        #if it is a single number and it is not 1 then we retur false 
        ans = 0
        seen = set()
        temp = n
        if n < 10 and n != 1:
            return False 
        while ans != 1:
            ans = 0
            while temp:
                last_digit = int(temp % 10)
                ans = int(ans + math.pow(last_digit, 2))
                temp = int(temp / 10)
            if ans in seen:
                return False
            else:
                seen.add(ans)
            print(ans)
            temp = ans
        return True 
