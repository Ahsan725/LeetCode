class Solution:
def removeDuplicates(s: str, k: int) -> str:
    """
    Remove all k consecutive duplicate characters from string s.
    
    For example:
    - s = "abcd", k = 2 returns "abcd" (no k duplicates)
    - s = "aa", k = 2 returns "" (2 consecutive 'a's removed)
    - s = "deeedbbcccbcadkic", k = 3 returns "aa"
    """
    stack = []
    
    # Process each character in the input string
    for current_char in s:
        # Check if stack is not empty and top element has the same character
        if stack and stack[-1][0] == current_char:
            # We found a match, so increment the count of consecutive characters
            character = stack[-1][0]
            count = stack[-1][1]
            new_count = count + 1
            stack[-1] = (character, new_count)
            
            # Check if we now have k consecutive duplicates
            if stack[-1][1] == k:
                # Remove this group since we have k consecutive characters
                stack.pop()
        else:
            # Current character is different from top of stack
            # Start a new group with this character and count 1
            new_group = (current_char, 1)
            stack.append(new_group)
    
    # Reconstruct the final string from the stack
    result = ""
    for character, count in stack:
        result = result + (character * count)
    
    return result


# Example usage:
# removeDuplicates("abcd", 2) → "abcd"
# removeDuplicates("aa", 2) → ""
# removeDuplicates("deeedbbcccbcadkic", 3) → "aa"