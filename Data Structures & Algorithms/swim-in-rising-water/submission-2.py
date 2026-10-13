"""
UMPIRE Strategy:
Understand: 
we have a sqaure grid of elevations. we start at the top-left and can move up, down, left, and right. we return the lowest water level that lets us reach the bottom-right.
Input_ grid, a list of lists of distinct integers
Output - an integer - the min time which is also the required water level
Constraints:
elevations are nonnegative
bounded by n^2
1 <=n <= 50

Clarifying questions:
1. can swim immediately
2. 
Match: DFS + binary search

Plan:
Brute force: try each integer water level, starting at the higher of the starting and ending elevations. at each level, id use DFS to check whether we can cross. I'd return the first level that works.
time complexity: O(n^4). there are R water levels to try, and each DFS might check all n^2 cells. we elevations bounded by n^2, time could be O(n^4)

DFS + binary search plan:
1. set left to the higher of thr starting and ending elevations
set right to the highest elevation in the grid
write a dfs helper that checks whether we can cross at a given wate rlevel
in dfs, start with (0,0) ina. stack and visited set

space: O(n^2)
Implement:
Review:
Evaluate:
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minHeap = [[grid[0][0], 0, 0]]
        visited = set() #keep track of the cells we've already visited
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while minHeap:
            #get the lowest water level first
            water, r, c = heapq.heappop(minHeap)

            if (r,c) in visited:
                continue
            
            visited.add((r,c))

            if r == n-1 and c == n-1: #reached the bottom right cell
                return water
            
            for dr, dc, in directions:
                row = r+dr
                col = c+dc

                if row < 0 or row >=n or col < 0 or col>=n:
                    continue
                
                if (row,col) in visited: 
                    continue
                
                #water must cover both our path so far and the next call
                next_water = max(water, grid[row][col])

                heapq.heappush(minHeap, [next_water, row, col])

        