"""Understand:
Flood fill is like using the paint bucket tool in image editors. Starting from a pixel, we want to change its color and spread to all connected pixels of the same original color. This naturally maps to a graph traversal problem where each pixel is a node connected to its four neighbors.

DFS works well here because we recursively explore as far as possible in one direction before backtracking. By changing the color as we visit each pixel, we mark it as visited, preventing infinite loops. If the new color equals the original, we skip the operation entirely to avoid unnecessary work.

Algorithm
1. Store the original color of the starting pixel.
2. If the original color equals the new color, return immediately (no work needed).
3. Define a recursive dfs function that takes row and column coordinates.
4. In dfs: if out of bounds or the pixel color does not match the original, return.
5. Otherwise, change the pixel to the new color and recursively call dfs on all four neighbors (up, down, left, right).
6. Start dfs from the initial coordinates and return the modified image.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orig = image[sr][sc] #store the og color of starting pixel
        if orig == color: 
            return image
        
        m, n = len(image), len(image[0])
        #m = number of rows
        #n = number of columns in the first row

        #define a recursive dfs function that takes row and column coordinates
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >=n or image[r][c] != orig: #if out of bounds or pixel color doesn't match
                return

            image[r][c] = color
            dfs(r + 1, c) #down
            dfs(r - 1, c) #up
            dfs(r, c + 1) #right
            dfs(r, c - 1) #left

        dfs(sr, sc)
        return image
        