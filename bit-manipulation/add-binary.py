class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""

        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2

        if carry:
            res = '1' + res 
        return res 
