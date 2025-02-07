from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balltocolor = {}  # Maps balls to their current color
        color_count = {}  # Keeps track of how many balls have each color
        res = []
        unique_colors = 0  # Tracks number of unique colors in use

        for ball, color in queries:
            # If the ball already had a color, reduce count of the previous color
            if ball in balltocolor:
                prev_color = balltocolor[ball]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    unique_colors -= 1  # The color is no longer used
            
            # Assign the new color
            balltocolor[ball] = color
            
            # If this color is new, increment count
            if color not in color_count or color_count[color] == 0:
                unique_colors += 1

            color_count[color] = color_count.get(color, 0) + 1

            res.append(unique_colors)

        return res
