"""
Understand:
we're given a sqaure grid of elevations. we start at the top-left cell and wnt to reach the bottom-right cell. we return the earliest time when the water is high enough for us to get there.
Calrifying questions:
1. just up and down
2. grid length can be between 1 and 50 so it won't be zero

Match: graph problem & min-heap
Plan:
brute force:
try every possible path without revisiting cells on the same path. for each path, i'd track it's highest elevation. then I'd return the smallest of those maximums.
- there can be exponentially many paths as the grid grows so this approach would be too slow
- the current path and recursion could take O(n^2) space as there are n^2 cells

instead of trying every path, we could use a min-heap to explore whiever option needs the lowest water first.

1. create a min-heap containing the starting cell and its elevation
2. create an empty visited set
3. while the heap has cells, pop the one with the smallest required water level
4. if we already visited that cell, we skip it or otherwise mark it as visited
5. if its the bottom right cell, return its required water level
6. check its four neighbors- up, down, left, and right
7. for each valid and unvisited neighbor, push [max(water_needed, neighbor_heights), row, column]
Implement: see below
Review:
grid = [
[0, 2]
[2, 2]
]
minHeap = [[0,0,0]]
we pop the starting cell (0,0) and mark it visited. it's water level is 0
both have elevation 2 so we push [2, 0, 1] and [2, 1, 0]
we pop (0,1) with water level 2. 
then we push [2,1,1] because max of (2,2) = 2

Evaluate:
time - O(n^2 log(n^2)) -> O( n^2 log n)
space: O(n^2)
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

        