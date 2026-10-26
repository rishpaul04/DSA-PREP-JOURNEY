class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        empty_count = 0
        start_r, start_c = 0, 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    empty_count += 1
                elif grid[r][c] == 0:
                    empty_count += 1

        def backtrack(r: int, c: int, remaining: int) -> int:
            if grid[r][c] == 2:
                return 1 if remaining == 0 else 0

            temp = grid[r][c]
            grid[r][c] = -1
            paths = 0

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] >= 0:
                    paths += backtrack(nr, nc, remaining - 1)

            grid[r][c] = temp
            return paths

        return backtrack(start_r, start_c, empty_count)