class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is an empty string, return an empty string since there's nothing to search for.
        if t == "":
            return ""
        
        # Initialize dictionaries to count characters in t and the current window in s.
        countT, window = {}, {}

        # Fill countT with the frequency of each character in t.
        for c in t:
            countT[c] = 1 + countT.get(c, 0)  # Increment the count of each character in t.

        # Variables to track how many characters we've matched and how many we need to match.
        have = 0  # Number of characters in the window that meet or exceed the frequency in t.
        need = len(countT)  # Total number of unique characters in t that need to be matched.

        # Initialize result variables. res will store the start and end indices of the minimum window.
        res = [-1, -1]  # Start and end indices of the best (smallest) window found.
        reslen = float("infinity")  # Length of the best window, initially set to infinity.
        l = 0  # Left pointer of the window.

        # Expand the window by moving the right pointer (r) through the string s.
        for r in range(len(s)):
            c = s[r]  # Character at the current right pointer position.
            window[c] = 1 + window.get(c, 0)  # Update the count of this character in the window.

            # If this character's frequency in the window matches its frequency in t, increment 'have'.
            if c in countT and window[c] == countT[c]:
                have += 1

            # When we have all the characters required (have == need), try to shrink the window from the left.
            while have == need:
                # Update the result if the current window is smaller than the previous best window.
                if (r - l + 1) < reslen:
                    res = [l, r]  # Update the start and end indices of the best window.
                    reslen = (r - l + 1)  # Update the length of the best window.

                # Pop the leftmost character from the window and update the window dictionary.
                window[s[l]] -= 1
                # If removing this character causes its count in the window to be less than its count in t,
                # decrement 'have' since we no longer have a valid match for this character.
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1  # Move the left pointer to the right, shrinking the window.

        # After the loop, if a valid window was found, return the substring. Otherwise, return an empty string.
        l, r = res  # Get the start and end indices of the best window.
        return s[l:r+1] if reslen != float("infinity") else ""  # Return the minimum window or an empty string.
