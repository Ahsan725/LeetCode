class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            summ = 0
            for c in str(num): #38
                summ += int(c) #3 + 8 -> 11   
            num = summ # num = 3
        
        return num

        