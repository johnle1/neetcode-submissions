class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = deque()

        directions = [[0,1], [0,-1], [1,0],[-1,0]]

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    freshRow,  freshCol = r + dr, c + dc
                    if freshRow < 0 or  freshCol < 0 or freshRow >= row or freshCol >= col or grid[freshRow][freshCol] != 1:
                        continue
                    grid[freshRow][freshCol] = 2
                    q.append([freshRow,freshCol])
                    fresh -= 1 
            time += 1
        return time if fresh == 0 else  -1








        