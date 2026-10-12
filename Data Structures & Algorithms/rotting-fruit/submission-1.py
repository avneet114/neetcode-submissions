"""
Understand: 
given a 2-d matrix grid. each cell can have one of three possible values
0 - empty
1 - fresh fruit
2 - rotten
every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then fresh fuit becomes rotten asw

return the min number of minutes that must elpase until there are fresh fruits remaining.
if impossible -> return -1
Match: multi source BFS problem
all rotten oranges start spreading at the same time to their neighboring fresh oranges
each bfs level represents 1 minute
if a fresh orange is reached, it becomes rotten in the next minute

key ideas:
- start BFS from all rotten oranges together
- count how many fresh oranges are there
- each bfs layer = one unit of time
- if any fresh orange is left at the end - answer -1

Plan:
1. intitialize a queue with positions of all rotten ornages
2. count total number of fresh oranges
3. while the queue is not empty and fresh oranges exist:
- process all nodes in the queue (one BFS lebvel)
- for each rotten ornage:
- check its 4 neighbors
- if a neighbor if fresh -> we make it rotten, decrease fresh count, add it to the queue
- increment time by 1
4. if fresh count become 0, return time
5. otherwise return -1 (some oranges never rot)
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #store the number of rows and column in the grid
        ROWS = len(grid)
        COLS = len(grid[0])

        #queue for rotten fuits; each item in a (row, column) position
        q = deque()

        #count how many fresh fruits exist
        fresh = 0

        #number of mins that have passed
        time = 0

        #find all initially rotten fruits and count fresh fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        #directions for moving up, down, left, right
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        #continue while there are fresh fruits and rotten fruits available
        while fresh > 0 and q:
            #save the number of rotten fruits at the current minute
            length = len(q)

            #process every rotten fruit from this minute
            for i in range(length):
                r, c = q.popleft()
            
                #check all four neighboring cells
                for dr, dc, in directions:
                    row, col = r + dr, c + dc

                    #skip positions outside the grid or cells that are not fresh
                    if (
                        row < 0
                        or row >=ROWS
                        or col < 0
                        or col >= COLS
                        or grid[row][col] != 1
                    ):
                        continue
                        #make fresh fruit rotten
                    grid[row][col] = 2

                        #process this fruit during the next minute
                    q.append((row,col))
                        # one fewer fresh fruit remains
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1

        