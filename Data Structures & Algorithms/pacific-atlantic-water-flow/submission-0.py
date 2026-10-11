"""
Understand: Pacific Atlantic Water Flow
instead of can water flow from this cell to an ocean?
reverse the direction:
starting from the ocean, which cells can we reach?

water normally flows 
- up, down, left, or right
- from a cell to a neighboring cell with height less than or equal to the current cell

the pacific ocean touches:
- top border and left border

the atlantic ocean touches 
- bottom border and right border

we need to return every cell from which water can reach both oceans

Match: graph traversal problem 
each grid cell is a graph node, and neighboring cells are connected if water can flow between them

a direct approach would start DFS from every cell and check whether it reaches both oceans. that could repeat a lot of work.

a better pattern is reverse DFS from the oceans:
- start DFS from pacific border cells
- start DFS from atlantic border cells
- find cells reached by both DFS traversals

Plan:
instead of starting DFS from every cell (slow), we reverse the thinking:

start from ocean borders and move uphill/flat (to neighbors with height >= current)

if u can climb from the ocean to a cell, then that cell can flow down to that ocean

so we do 2 DFS runs:
- from all pacific border cells (top row+left column) -> mark all reachable cells in pac
- from atlantic border cells (bottom row+ right column) -> mark all reachable cells in atl

answer = cells that are in both sets

algorithm:
1. create two visited sets: pac, atl
2. dfs rule (reverse flow):
- from cell (r,c), you may go to a neighbor (nr, nc) only if heights[nr][nc] >=heights[r][c] -> uphill or same
3. run DFS from EVERY pacific border cell, fill pac
4. run DFS from every atlantic border cell, fill atl
5. for every cell in the grid, if it's in both pac, atl, add it to result
6. return result

"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        #create two visited sets: pac, atl
        pac = set() #visit
        atl = set() #visit

        def dfs(r, c, visit, prevHeight):
            #stop if current cell is invalid
            if ((r,c) in visit or r<0 or r== ROWS or c<0 or  c == COLS or heights[r][c] < prevHeight):
                return
            
            visit.add((r,c)) #mark this cell as reachable from current ocean
            #explore all diff directions
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        #try every cell in the left and right columns
        for r in range(ROWS):
            #the left column borders the pac ocean
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1]) #the right column border the atlantic ocean

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
            #store cells that can reach both oceans in this
        res = []
            #check every cell in grid now
        for r in range(ROWS):
            for c in range(COLS):
                # a cell belongs in the answer if both oceans can reach it
                if (r, c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

        