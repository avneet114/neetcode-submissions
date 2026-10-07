"""
Using UMPIRE strategy:
Understand:
Think of the grid as a map where '1' is land and '0' is water.
An island is a group of connected land cells (up, down, left, right).
Whenever we find a land cell that hasn’t been visited, we start a DFS to sink the entire island by marking all its connected land as water. Each DFS call corresponds to one island.

Match: DFS
Plan:
Iterate through every cell in the grid.
When a cell with value '1' is found:
Increment the island count.
Run DFS from that cell.
In DFS:
If the cell is out of bounds or is '0', return.
Mark the current cell as '0' (visited).
Recursively explore all 4 directions (up, down, left, right).
Continue until all cells are processed.
Return the total island count.
Implement:
Review
Evaluate:
Time: O(m*n)
Space: O(m*n) where m is the number of rows and n is the number of columns in the grid
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]] #down up right left
        if not grid or not grid[0]:
            return 0 #handle empty grid

        #store the number of rows and cols
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0 #keep track of how many separate islands we find

        def dfs(r, c): #define a recursive DFS function that explores all land cells connected to position r,c
            if (
                r < 0 
                or c < 0 
                or r>= ROWS 
                or
                c >= COLS 
                or grid[r][c] == "0"): #outside the grid or is water, stop
                return
            

            grid[r][c] = "0" #mark current cell as visited by chanfing it to water
            #visit all four neighboring cells
            for dr, dc in directions:
                dfs(r + dr, c + dc) #add each direction
        
        #r = current row
        #c = current column

        #dr = row change
        #dc = col change -> how much to move from current cell
        for r in range(ROWS):
            for c in range(COLS):
                #found a new, unvisited island
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1 #if cell is land, it must be starting point of new island because any connected island would alr have been changed to 0 by prev DFS
        return islands
        