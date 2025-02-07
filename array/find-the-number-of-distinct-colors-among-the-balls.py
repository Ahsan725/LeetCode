from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balltocolor = {}  # Maps balls to their assigned color
        unique_colors = set()  # Tracks unique colors in use
        res = []

        for ball, color in queries:
            # If the ball already had a color, remove the old color
            if ball in balltocolor:
                old_color = balltocolor[ball]
                unique_colors.discard(old_color)  # Remove previous color if present

            # Assign new color to ball
            balltocolor[ball] = color
            unique_colors.add(color)  # Ensure the color is counted

            res.append(len(unique_colors))  # Count of unique colors used so far

        return res
