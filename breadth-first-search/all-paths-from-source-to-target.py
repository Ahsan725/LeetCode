from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph) - 1  # The last node we want to reach

        def dfs(path: List[int], node: int):
            if node == target:
                result.append(path[:])  # Found a path, make a copy and save it
                return
            for neighbor in graph[node]:
                dfs(path + [neighbor], neighbor)  # Explore next step

        dfs([0], 0)  # Start DFS from node 0
        return result
