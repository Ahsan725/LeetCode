class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string = (str.strip(s)).lower()
        string = ''.join(e.lower() for e in s if e.isalnum())
        # string = string.lower()

        left = 0
        right = len(string) - 1
        while(left <= right):
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
        