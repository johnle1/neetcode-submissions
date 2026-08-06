class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        dp = [[False for _ in range(col)] for _ in range(row)]

        max_island_size = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r >= row or c >= col:
                return 0
            if grid[r][c] == 0 or dp[r][c]:
                return 0
            dp[r][c] = True
            return (1 + 
            dfs(r, c - 1) + 
            dfs(r, c + 1) + 
            dfs(r + 1, c) + 
            dfs(r - 1, c))
        for c in range(col):
            for r in range (row):
                if grid[r][c] == 1 and not dp[r][c]:
                    island_size = dfs(r,c)     
                    max_island_size = max(island_size, max_island_size)  
        return max_island_size
        