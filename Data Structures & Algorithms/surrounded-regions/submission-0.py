class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
            
        row, col = len(board), len(board[0])
        
        # 1. Define the DFS function to mark safe "O"s
        def dfs(r, c):
            # Base case: Stop if out of bounds OR if the cell is not "O"
            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != "O":
                return
            
            # Mark the current "O" as a temporary letter "T" (Safe zone)
            board[r][c] = "T"
            
            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 2. Run DFS only on the borders of the board
        for r in range(row):
            dfs(r, 0)           # Left column
            dfs(r, col - 1)     # Right column
            
        for c in range(col):
            dfs(0, c)           # Top row
            dfs(row - 1, c)     # Bottom row

        # 3. Clean up the board
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    # Any remaining "O" was completely surrounded, capture it
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    # Restore the safe boundary regions back to "O"
                    board[r][c] = "O"