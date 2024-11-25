from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        start = ''.join(str(cell) for row in board for cell in row)
        target = "123450" 

        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        
        queue = deque([(start, start.index('0'), 0)]) 
        visited = set()
        visited.add(start)
        
        while queue:
            state, zero_idx, steps = queue.popleft()
            if state == target:
                return steps
            for move in moves[zero_idx]:
                new_state = list(state)
                new_state[zero_idx], new_state[move] = new_state[move], new_state[zero_idx]
                new_state_str = ''.join(new_state)
                
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, move, steps + 1))
        return -1
  # https://leetcode.com/problems/sliding-puzzle/
