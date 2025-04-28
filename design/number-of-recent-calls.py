class RecentCounter:
    def __init__(self):
        self.reqs = deque()

    def ping(self, t: int) -> int:
        self.reqs.append(t)

        left_boundary = t - 3000
        while self.reqs[0] < left_boundary:
            self.reqs.popleft()     # O(1) each, amortised

        return len(self.reqs)
