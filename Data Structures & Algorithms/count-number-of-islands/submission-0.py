class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
    
        row, col = len(grid), len(grid[0])
        num_island = 0
        dp = [[False for _ in range(col)] for c in range(row)]

        def dfs(r,c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0" or dp[r][c]:
                return

            
            dp[r][c] = True

            left = dfs(r, c-1)
            right = dfs(r, c+1)
            down = dfs(r+1, c)
            up = dfs(r-1,c)

        for r in range (row):
            for c in range (col):
                if grid[r][c] == "1" and not dp[r][c]:
                    num_island += 1
                    dfs(r,c)
        return num_island
                    
        
        