# class RecentCounter:
#     def __init__(self):
#         self.reqs = deque()

#     def ping(self, t: int) -> int:
#         self.reqs.append(t)

#         left_boundary = t - 3000
#         while self.reqs[0] < left_boundary:
#             self.reqs.popleft()     # O(1) each, amortised

#         return len(self.reqs)


#another solution. This runs in O(log n) better for interviews
class RecentCounter:
    def __init__(self):
        # pings arrive in non-decreasing order, so the list is always sorted
        self.reqs = []

    def ping(self, t: int) -> int:
        self.reqs.append(t)

        left_boundary = t - 3000           # earliest time we still care about
        n = len(self.reqs)

        # --- manual binary search for first index ≥ left_boundary ---
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.reqs[mid] < left_boundary:
                lo = mid + 1              # too small → search right half
            else:
                hi = mid - 1              # mid works, but keep looking left

        first_valid = lo                  # first index whose value ≥ left_boundary
        # -------------------------------------------------------------

        return n - first_valid            # all elements from first_valid .. n-1 are in range

