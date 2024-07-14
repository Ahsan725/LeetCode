class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Initialize variables
        max_length = 0
        path_length = {0: 0}  # Depth 0 with path length 0 (for root directory)

        # Split the input by new lines to process each line separately
        for line in input.split('\n'):
            # Find the depth (number of tabs)
            depth = line.count('\t')
            # Remove the tab characters to get the actual name
            name = line.lstrip('\t')
            # Check if it's a file
            if '.' in name:
                # It's a file, calculate the full path length
                max_length = max(max_length, path_length[depth] + len(name))
            else:
                # It's a directory, update the current path length for this depth
                path_length[depth + 1] = path_length[depth] + len(name) + 1  # +1 for the '/' character

        return max_length

# Example usage:
solution = Solution()
input1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(solution.lengthLongestPath(input1))  # Output: 20

input2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(solution.lengthLongestPath(input2))  # Output: 32

input3 = "a"
print(solution.lengthLongestPath(input3))  # Output: 0
