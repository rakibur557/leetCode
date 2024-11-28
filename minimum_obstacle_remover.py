from collections import deque

class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Priority queue for 0-1 BFS
        queue = deque([(0, 0, 0)])  # (row, col, obstacles_removed)
        visited = [[False] * n for _ in range(m)]
        
        while queue:
            row, col, removed = queue.popleft()
            
            if row == m - 1 and col == n - 1:  # Reached bottom-right corner
                return removed
            
            if visited[row][col]:
                continue
            
            visited[row][col] = True
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if grid[nr][nc] == 0:
                        queue.appendleft((nr, nc, removed))  # No obstacle, prioritize
                    else:
                        queue.append((nr, nc, removed + 1))  # Add obstacle removal count
        
        return -1  # No valid path found


# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/