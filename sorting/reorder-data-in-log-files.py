from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def getKey(log):
            # Split the log into two parts: identifier and the rest
            identifier, rest = log.split(" ", 1)
            # Check if it's a digit log or letter log
            if rest[0].isdigit():
                # Return a tuple that ensures digit logs come after letter logs
                return (1,)
            else:
                # Return a tuple with 0 to ensure letter logs come first,
                # followed by the content and then the identifier for sorting
                return (0, rest, identifier)

        # Use sorted with the custom key
        return sorted(logs, key=getKey)
