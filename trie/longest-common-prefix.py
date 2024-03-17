class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #initial observations:
        # we will have to correct these
        #iterate over each word in the array for the first letter first
        #if the first letter matches in every word then move on to the second
        """
Iterating through Characters:
for chars in zip(*strs):
We use zip(*strs) to iterate through the characters of each string simultaneously. This creates an iterator that yields tuples containing characters at the same index across all strings.
First Iteration:

The first tuple yielded by zip contains the first characters of all strings:
chars = ('f', 'f', 'f')
Since all characters in this tuple are the same, we append the first character ('f') to the prefix:
prefix += chars[0]
# prefix = 'f'
Second Iteration:

The second tuple yielded by zip contains the second characters of all strings:
chars = ('l', 'l', 'l')
Again, all characters in this tuple are the same, so we append the second character ('l') to the prefix:
prefix += chars[0]
# prefix = 'fl'
Third Iteration:

The third tuple yielded by zip contains the third characters of all strings:
chars = ('o', 'o', 'i')
In this tuple, characters differ across strings. Since they are not all the same, we break out of the loop and return the current prefix, which is 'fl'.

        """
        if not strs:
            return ""

        prefix = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break
        return prefix