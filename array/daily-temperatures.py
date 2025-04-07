'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days 
you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #how can we translate what we have to do and use a ds to help 
        #[73, 74, 75, 71,]
        #[1, 1 , 4, 2 ]

        #I need a variable to keep track of the item we have to process next
        # a loop tp keep adding until we find a bigger value 
        #a variable counter to track how many days til next warmer day

				
        #time: O(n) -> O(n)
        #Space: O(n)
        stack = []
        nxt_item = 0 #keeps track of the next item we have to process  
        res = []
        
        while nxt_item < len(temperatures):
            cur = temperatures[nxt_item] 
            idx = nxt_item
            nxt_item += 1 
            count = 0
            while temperatures[idx] <= cur:
                stack.append(temperatures[idx])
                count += 1
                idx += 1
            res.append(count)
            while stack[-1] != temperature[nxt_item]:
              stack.pop()
              
        # ---------------------------------------------------------------
        n  = len(temperatures)
        res = [0] * n
        stack = [] # [temp, idx]
        #  [73,74,75,71,69,72,76,73]
        [
          (73, 0)
          (74)
          
        ]
        
        for i, tmp in enumerate(temperatures):
					while stack and stack[-1][0] < tmp:
            tmp, idx = stack.pop()
            res[idx] = i - idx
          stack.append([tmp, i])
              
        return res 
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
              
            