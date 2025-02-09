class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build a mapping from each course to its prerequisites.
        premap = defaultdict(list)
        for course, pre in prerequisites:
            premap[course].append(pre)
        
        # Set to keep track of courses in the current DFS path (for cycle detection)
        visiting = set()
        
        def dfs(course: int) -> bool:
            # If we're already visiting this course, we've detected a cycle.
            if course in visiting:
                return False
            # If this course has no prerequisites, it's safe to take.
            # (Also acts as a memoization since we clear the prerequisites list when done)
            if premap[course] == []:
                return True
            
            # Mark the course as being visited
            visiting.add(course)
            
            # Check all prerequisites for the current course.
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            
            # Remove the course from the visiting set as we are done processing it.
            visiting.remove(course)
            
            # Clear the prerequisites list to mark the course as processed.
            premap[course] = []
            return True
        
        # Run DFS on every course. Note: We run DFS on courses 0 to numCourses - 1.
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
