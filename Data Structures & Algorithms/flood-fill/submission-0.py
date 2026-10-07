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
        