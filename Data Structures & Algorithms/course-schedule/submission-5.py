"""
Understand: given an array prereq where prereq[i] = [a, b] means u must take course b first if u wanna take course a
numCourses - courses u are required to take w length numCourses - 1, return true if it's possble to finish all courses, otherwise return false
Constraints:
- there's at least 1 course u must take
- prereqs can be 0
- all prereqs pairs are unique

each course is a node and each prereq is a directed edge. we can fiish all courses ONLY if there's no cycle in this directed graph
a cycle means -> course A needs course B
course B needs C
C needs A so we're stuck forever
Match: DFS Graphs
while doing DFS, we keep track of courses in current recursion path
if we visit a course already in the current path -> cycle found
if a course has no prereqs left, it's safe
Plan:
1. build a graph where each course points to it prereqs
2. use a visiting set to track the current DFS path
3. for each course
- run dfs
- if the course is already in visiting, return false (cycle)
- recursively DFS its prereqs
4. after successfully processing a course, clear its prereqs list (mark as done)
5. if all courses are processed without cycles, return true

if it's a cycle -> impossible to complete the courses
Implement
Review: O(V+E), where v is the number of courses(nodes) and e is the number of prereqs(edges)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each course to its prereqs
        preMap = {i:[] for i in range(numCourses)} #every course initially -> map it into an empty list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        #visiySet = all courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []: #prereqs have empty list
                return True
            
            visitSet.add(crs) #take course and add it to list
            for pre in preMap[crs]:
                if not dfs(pre): return False

            visitSet.remove(crs)
            preMap[crs] = []
            return True
        #some courses maybe disconnected from one another, check every course.
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        
