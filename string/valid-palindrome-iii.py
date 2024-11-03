class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # Dictionary to store results of (left, right, counter) states
        memo = {}

        def verify(s, left, right, counter=0):
            # If this state has been computed before, return the stored result
            if (left, right, counter) in memo:
                return memo[(left, right, counter)]

            # Check for k-palindrome with up to k allowed removals
            while left < right:
                if s[left] != s[right]:
                    if counter < k:
                        # Attempt to skip either left or right character
                        result = verify(s, left + 1, right, counter + 1) or verify(s, left, right - 1, counter + 1)
                        memo[(left, right, counter)] = result
                        return result
                    else:
                        memo[(left, right, counter)] = False
                        return False
                else:
                    left += 1
                    right -= 1

            # If pointers cross without using more than k skips, it’s a valid k-palindrome
            memo[(left, right, counter)] = True
            return True

        # Start recursive check from both ends of the string
        return verify(s, 0, len(s) - 1)