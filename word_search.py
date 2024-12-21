class Solution(object):
    def exist(self, board, word):
    
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, index):
            # If all characters are found
            if index == len(word):
                return True
            # Check boundaries and character match
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
                return False
            
            # Mark the cell as visited
            temp, board[r][c] = board[r][c], '#'
            
            # Explore all possible directions
            res = (
                backtrack(r + 1, c, index + 1) or  # Down
                backtrack(r - 1, c, index + 1) or  # Up
                backtrack(r, c + 1, index + 1) or  # Right
                backtrack(r, c - 1, index + 1)    # Left
            )
            
            # Restore the cell value after backtracking
            board[r][c] = temp
            
            return res
        
        for row in range(rows):
            for col in range(cols):
                # Start the backtracking if the first character matches
                if board[row][col] == word[0] and backtrack(row, col, 0):
                    return True
        
        return False
    
# https://leetcode.com/problems/word-search
