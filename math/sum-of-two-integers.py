class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # Mask to get last 32 bits
        MAX_INT = 0x7FFFFFFF  # Max positive 32-bit integer

        x = a & MASK
        y = b & MASK

        #this is the actual code above was python specific int problems
        while y != 0:
            car = (x & y) << 1
            x = x ^ y
            y = car & MASK  # Ensure it remains 32-bit

        # Convert to a signed integer if the result exceeds MAX_INT
        return x if x <= MAX_INT else ~(x ^ MASK)
