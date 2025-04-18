from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        email_graph = defaultdict(set)      # now using set
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_graph[first_email].add(email)
                email_graph[email].add(first_email)
                email_to_name[email] = name

        visited = set()
        res = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for neighbor in email_graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for email in email_graph:
            if email not in visited:
                component = []
                dfs(email, component)
                res.append([email_to_name[email]] + sorted(component))

        return res
