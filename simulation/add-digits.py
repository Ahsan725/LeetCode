class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            summ = 0
            for c in str(num):
                summ += int(c)
            num = summ
        return num 