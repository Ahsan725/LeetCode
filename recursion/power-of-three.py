class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        prod_map = {}
        
        for x in range(31):
            if n in prod_map:
                return True
            product = 3 ** x
            if product == n:
                return True
            prod_map[product] = x
        return False
        
            
            
        