class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        maxodd = float('-inf')
        mineven = float('inf')

        for letter, frequency in freq.items():
            if frequency % 2 == 0:
                #means even
                mineven = min(mineven, frequency)
            else:
                #means odd
                maxodd = max(maxodd, frequency)
        return maxodd - mineven 
        