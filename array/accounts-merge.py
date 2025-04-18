#the right way to solve this is either using a union find or dfs
class Solution:
    def accountsMerge(self, accounts):
        email_to_name = {}
        merged_accounts = []

        # This list will store sets of emails that have already been grouped
        groups = []

        for acc in accounts:
            name = acc[0]
            emails = set(acc[1:])
            matched_groups = []
            
            # Check existing groups for any email overlap
            for i, group in enumerate(groups):
                if emails & group:
                    matched_groups.append(i)

            # If no group matches, create a new one
            if not matched_groups:
                groups.append(emails)
                for email in emails:
                    email_to_name[email] = name
            else:
                # Merge all matched groups with current emails
                new_group = emails.copy()
                for i in reversed(matched_groups):  # reverse to safely remove by index
                    new_group |= groups[i]
                    groups.pop(i)
                groups.append(new_group)
                for email in new_group:
                    email_to_name[email] = name  # optional: last name seen wins

        # Build final result
        for group in groups:
            sample_email = next(iter(group))
            name = email_to_name[sample_email]
            merged_accounts.append([naafrom collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        email_graph = defaultdict(list)      # email -> list of connected emails
        email_to_name = {}                   # email -> name

        # Step 1: Build the graph
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_graph[first_email].append(email)
                email_graph[email].append(first_email)
                email_to_name[email] = name

        visited = set()
        res = []

        # Step 2: DFS to find connected components (email groups)
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
me] + sorted(group))

        return merged_accounts
