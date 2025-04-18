from collections import defaultdict

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
            merged_accounts.append([name] + sorted(group))

        return merged_accounts
