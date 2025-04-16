class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #create a graph
        """
        this problem has two parts create a graph because that will allow us to traverse the parent as well. You use a q and to use bfs and a graph as a default dict
        if you
        """

        q = deque([root])
        graph = defaultdict(list)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    graph[node].append(node.left)
                    graph[node.left].append(node)
                    q.append(node.left)
                if node.right:
                    graph[node].append(node.right)
                    graph[node.right].append(node)
                    q.append(node.right)
        
        res = []
        seen = set([target])

        q2 = deque([(target, 0)])
        while q2:
            for _ in range(len(q2)):
                node, distance = q2.popleft()

                if distance == k:
                    res.append(node.val)
                else:
                    for edge in graph[node]:
                        if edge not in seen:
                            seen.add(edge)
                            q2.append((edge, distance + 1))
        return res 
