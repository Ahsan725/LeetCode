class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # import requests
# import mysql.connector
# import pandas as pd
# a function that takes two numbers but these number can be pretty big could overflow -> add these two numbers
# peeking under the hood, how would you go about it implementing such a functionality
# integer value 

#approach: 
        str1 = num1
        str2 = num2

        n = len(str1) #rerurns the length
        m = len(str2)
        numOfZeroes = 0
        
        if n > m:
            numOfZeroes = n-m
            for i in range(numOfZeroes):
                str2 = '0'+str2
        else:
            numOfZeroes = m-n
            for i in range(numOfZeroes):
                str1 = '0'+str1
        
        
        # 4-> 0
        #3245 -> 4
        #0341 -> 4
        # string result 
        #555
        #555
        
        result = ''
        carry = 0 
        for i in range(len(str1)-1, -1, -1):
            sum = int(str1[i]) + int(str2[i]) + carry
            carry = 0
            if sum >= 10:
                carry +=1
                sum = sum - 10
            result = str(sum)+result
        if carry > 0:
            result = str(carry) + result
        # prepend carryover
        
        return result