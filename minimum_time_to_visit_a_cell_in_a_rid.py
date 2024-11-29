import heapq

class Solution(object):
    def minimumTime(self, grid):
        m, n = len(grid), len(grid[0])
        
        # If the second cell is inaccessible, return -1
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        # Min-heap for Dijkstra's algorithm: (time, row, col)
        heap = [(0, 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Visited set to keep track of visited cells
        visited = set()
        
        while heap:
            time, row, col = heapq.heappop(heap)
            
            # If we've reached the bottom-right corner
            if (row, col) == (m - 1, n - 1):
                return time
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            # Explore neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited:
                    # Wait until the time requirement of the cell is met
                    wait_time = max(0, grid[new_row][new_col] - (time + 1))
                    new_time = time + 1 + wait_time
                    
                    # Ensure proper time adjustment for oscillating cells
                    if wait_time > 0 and (wait_time % 2 == 1):
                        new_time += 1
                    
                    heapq.heappush(heap, (new_time, new_row, new_col))
        
        return -1

# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid