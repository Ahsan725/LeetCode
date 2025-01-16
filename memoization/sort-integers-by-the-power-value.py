class Solution:

    def getKth(self, low: int, high: int, k: int) -> int:
        # Dictionary to memoize calculated power values
        power_cache = {}

        # Helper function to compute the power value of a number
        def calculate_power(num: int) -> int:
            # Base case: The power of 1 is 0
            if num == 1:
                return 0

            # If already calculated, return from cache
            if num in power_cache:
                return power_cache[num]

            # Calculate power recursively
            if num % 2 == 0:
                # Even number: next number is num / 2
                power_cache[num] = 1 + calculate_power(num // 2)
            else:
                # Odd number: next number is 3 * num + 1
                power_cache[num] = 1 + calculate_power(3 * num + 1)

            return power_cache[num]

        # Create a list of tuples (number, power value) for the range [low, high]
        number_power_pairs = [(num, calculate_power(num)) for num in range(low, high + 1)]

        # Sort the pairs by power value, and by number if power values are equal
        number_power_pairs.sort(key=lambda pair: (pair[1], pair[0]))

        # Return the k-th number in the sorted list (1-based index, so k - 1)
        return number_power_pairs[k - 1][0]