from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sum_count = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = sum(int(c) for c in str(i))
            digit_sum_count[digit_sum] += 1

        max_count = max(digit_sum_count.values())

        res = 0
        for count in digit_sum_count.values():
            if count == max_count:
                res += 1
                
        return res
