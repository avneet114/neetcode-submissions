#run dfs on every single island and keep track which one of them have max area
# then return that
# look at every single cell value -> if 1 -> run dfs
# use visit set so we dont run dfs on a cell again
"""
Understand: max area of island
An island is a group of connected 1s.
To find the maximum area, we explore each island fully and count how many cells it contains.

Depth First Search (dfs) helps us:

Start from a land cell
Visit all connected land cells (up, down, left, right)
Count the size of that island
Keep track of the largest size seen
We mark cells as visited so we don't count the same cell twice.

Algorithm
Initialize a visited set to track already counted cells.
For each cell in the grid:
If it is land (1) and not visited, run dfs from it.
dfs:
Stop if out of bounds, water (0), or already visited.
Mark the cell as visited.
Return 1 + area from all 4 neighbors.
After each dfs call, update the maximum area.
Return the maximum area found.
Plan: dfs 
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #store the number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])
        #keep track of land cells that have alr been visited
        visit = set()

        def dfs(r, c):
            #stop if the ell is outside grid, water,or alr visited
            if (r<0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r,c) in visit):
                return 0 #didn't find an island

            visit.add((r,c)) #add it to set to show it has been visited so it aint counted again
            return(1 + dfs(r+1, c)+ #returns the area of island connected to cell(r,c)
                    dfs(r-1, c)+
                    dfs(r, c+1)+
                    dfs(r, c-1)) # all 4 directions
        
        area = 0 #store the largest island area found so far
        #iterate ovewr entire grid
        for r in range(ROWS):
            for c in range(COLS): 
                #calculate the island area if this cell starts an unvisited island
                area = max(area, dfs(r, c))
        return area
        