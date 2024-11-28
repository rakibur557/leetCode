class Solution(object):
    def convert(self, s, numRows):
    
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        current_row = 0
        down = False

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                down = not down

            current_row += 1 if down else -1

        return ''.join(rows)
    
# https://leetcode.com/problems/zigzag-conversion