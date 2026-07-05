class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # dp_score[i][j] will store the max score to reach (i, j) from 'S'
        # dp_paths[i][j] will store the number of paths achieving that max score
        dp_score = [[-1] * n for _ in range(n)]
        dp_paths = [[0] * n for _ in range(n)]
        
        # Base case: start at the bottom-right corner 'S'
        dp_score[n-1][n-1] = 0
        dp_paths[n-1][n-1] = 1
        
        # Iterate backwards from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Skip the starting point initialization and obstacles
                if (i == n - 1 and j == n - 1) or board[i][j] == 'X':
                    continue
                
                max_neighbor_score = -1
                
                # Check the 3 valid incoming directions (down, right, down-right)
                directions = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]
                
                for ni, nj in directions:
                    if ni < n and nj < n and dp_score[ni][nj] != -1:
                        if dp_score[ni][nj] > max_neighbor_score:
                            max_neighbor_score = dp_score[ni][nj]
                            dp_paths[i][j] = dp_paths[ni][nj]
                        elif dp_score[ni][nj] == max_neighbor_score:
                            dp_paths[i][j] = (dp_paths[i][j] + dp_paths[ni][nj]) % MOD
                
                # If at least one neighbor was reachable, update current cell
                if max_neighbor_score != -1:
                    current_val = 0 if board[i][j] == 'E' else int(board[i][j])
                    dp_score[i][j] = max_neighbor_score + current_val
        
        # Extract the final results from the top-left corner 'E'
        if dp_score[0][0] == -1:
            return [0, 0]
        
        return [dp_score[0][0], dp_paths[0][0]]