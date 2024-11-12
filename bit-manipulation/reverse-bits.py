class Solution:
    def reverseBits(self, n: int) -> int:
        # Converts n to a 32-bit binary string, reverses the bits, then converts it back to an integer.
        
        binary_string = f"{n:032b}"  # Converts n to a 32-bit binary string representation.
        reversed_string = binary_string[::-1]  # Reverses the binary string.
        
        res = int(reversed_string, 2)  # Converts the reversed binary string back to an integer.
        
        return res  # Returns the integer with reversed bits.
