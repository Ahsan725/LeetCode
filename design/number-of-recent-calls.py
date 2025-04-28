class RecentCounter:

    def __init__(self):
        self.reqs = []

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        #calculate the range
        end = t
        start = t - 3000
        count = 0
        for num in self.reqs:
            if num >= start and num <= end:
                count += 1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)