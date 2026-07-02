class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]

        dq = deque()
        dist[0][0] = grid[0][0]
        dq.appendleft((0, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while dq:
            x, y = dq.popleft()

            if x == m - 1 and y == n - 1:
                return dist[x][y] < health

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    w = grid[nx][ny]

                    if dist[x][y] + w < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + w

                        if w == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        return dist[m - 1][n - 1] < health