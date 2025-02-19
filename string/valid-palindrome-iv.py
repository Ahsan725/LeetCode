class Solution:
    def makePalindrome(self, s: str) -> bool:
        def verify(s, left, right, counter=0):
            n = 2
            mismatch = 0  # Set n equal to k to allow up to k removals

            while left < right:
                if s[left] != s[right]:
                    # If there’s a mismatch and counter < k, try to remove either `s[left]` or `s[right]`
                    mismatch += 1
                    if mismatch > 3:
                        return False # If counter reaches k, no more removals allowed
                else:
                    left += 1
                    right -= 1
            return True  # If the loop completes, the string is a k-palindrome

        # Start the check with both pointers at the ends of the string
        return verify(s, 0, len(s) - 1)