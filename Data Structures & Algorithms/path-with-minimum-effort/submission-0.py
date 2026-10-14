"""
Understand: we want to go from top-left to bottom-right. for each move, we calculate the absolute difference between the two heights. the biggest difference on our route is its effort and we want the smallest possible effort
Input - heights, a list of lists of integers. the grid can have different numbers of rows and columns
Output - an integer representing the min effort 
we can move up, down, left right

clarifying questions:
1. atleast one cell
2. return 0 if there's one cell
3. repeats and negatives are are allowed/.

Edge cases:
- [[7] -> 0
- [[3,3] [3,3]] -> 0 cuz every move is between equal heights
- [[-3, -1]] -> 2, negatives work the same way
- [[1, 4, 2]] -> one route exists -> 3

Match: binary search + dfs
Plan:
brute force approach: 
let r be the number of rows
c be the columns
h be the largest height minus smallest height
time complexity - O((h+1) * r * c)
space: O(r*c)

optimal solution: dfs + binary search
1. store the number of rows and columns
2. set low = 0 and heigh = largest height - smallest height
3. create a helper , can_reach(limit) that starts dfs from (0,0) using a stack and visited set
4. in dfs, pop a cell. if it's the bottom-right, return true
5. check its four neighbors. add a neighbor if its inside the grid, unvisited, diff from current cell is at most limit. if dfs finished without reaching the end, we return false
6. while low < high, we try the middle effort. if dfs succeeds, we set high = mid and otherwise set low = mid+1
7. return low -> smallest effort that works

Implement: see below
Review:
heights = [
            [1, 1, 1]
            [3, 2, 4]
            [2, 5, 4]
]
low = 0 and high = 4
mid = 2
1 - 1 - 2 - 4 - 4 -> diff is at most 2
mid = 1
low = 2
Evaluate:
time - O(r * c * log(h+1)) for h >= 1
o (r*c) when h = 0
space - o(r*c)
let r be the number of rows
c be the columns
h be the largest height minus smallest height
"""

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def can_reach(limit):
            #start exploring from the top left cell
            stack = [(0,0)]
            visited = {(0,0)}

            while stack:
                r, c = stack.pop()

                if r == rows - 1 and c == cols - 1:
                    return True
                
                for dr, dc in directions:
                    row = r +dr
                    col = c + dc

                    #ignore position outside the grid
                    if row < 0 or row >= rows or col < 0 or col  >= cols:
                        continue
                    
                    #avoid checking the same cell again
                    if (row, col) in visited:
                        continue
                    
                    difference = abs(heights[row][col] - heights[r][c])

                    if difference <= limit:
                        visited.add((row, col))
                        stack.append((row, col))
            return False
        
        low = 0
        highest = max(max(row) for row in heights)
        lowest = min(min(row) for row in heights)
        high = highest - lowest

        while low < high:
            mid = (low+high) // 2

            if can_reach(mid):
                high = mid
            else:
                low = mid+1
        return low                    
                
        