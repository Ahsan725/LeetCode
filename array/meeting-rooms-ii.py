class Solution:
    def minMeetingRooms(self, intervals):
        endpoints = []
        for start, end in intervals:
            endpoints.append((start, 1))
            endpoints.append((end, -1))
        endpoints.sort()
        res = need = 0
        for _, delta in endpoints:
            need += delta
            res = max(res, need)
        return res