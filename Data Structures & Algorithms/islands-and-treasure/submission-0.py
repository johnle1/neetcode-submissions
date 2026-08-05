class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        dp = [[False for _ in range(col)]for _ in range(row)]
        q = deque()
        def addRoom(r,c):
            if r < 0 or c < 0 or r >= row or c >= col or dp[r][c] or grid[r][c] == -1:
                return
            dp[r][c] = True
            q.append([r,c])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append([r,c])
                    dp[r][c] = True
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r,c+1)
                addRoom(r-1,c)
                addRoom(r,c-1)
            dist += 1
        

        