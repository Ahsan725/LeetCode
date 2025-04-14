class Solution:
    def minMeetingRooms(self, intervals):
        # List to hold all start and end times marked with +1 (start) and -1 (end)
        timeline = []

        for start, end in intervals:
            timeline.append((start, 1))   # Meeting starts, need a room
            timeline.append((end, -1))    # Meeting ends, free a room

        # Sort events by time. If times are the same, end (-1) comes before start (+1)
        timeline.sort()

        current_rooms_in_use = 0
        max_rooms_needed = 0

        # Sweep through the timeline
        for time, change in timeline:
            current_rooms_in_use += change  # +1 if meeting starts, -1 if it ends
            max_rooms_needed = max(max_rooms_needed, current_rooms_in_use)  # Track the peak

        return max_rooms_needed
