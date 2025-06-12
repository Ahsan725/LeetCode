class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        graphh = {}
        for i, edges in enumerate(graph):
            graphh[i] = edges

        #dfs
        stack = [[0,0]]
        while stack:
            node, path = stack.pop()

            if node == n -1:
                res.append(path)
            for nei in graphh[node]:
                stack.append((nei, path + [nei]))

        return res