from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = grid[0][0]  # cost of standing on starting cell
        
        dq = deque([(0, 0)])
        
        while dq:
            x, y = dq.popleft()
            d = dist[x][y]
            
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nd = d + grid[nx][ny]
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if grid[nx][ny] == 1:
                            dq.append(nx, ny) if False else dq.append((nx, ny))  # cost 1 -> push to back
                        else:
                            dq.appendleft((nx, ny))  # cost 0 -> push to front
        
        return health - dist[m - 1][n - 1] > 0