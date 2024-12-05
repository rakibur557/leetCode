class Solution(object):
    def canChange(self, start, target):

        # Remove blank spaces and compare the sequences of L and R
        start_pieces = [c for c in start if c != '_']
        target_pieces = [c for c in target if c != '_']
        
        # The sequence of L and R must match
        if start_pieces != target_pieces:
            return False
        
        # Validate the positions of L and R
        start_indices = [(i, c) for i, c in enumerate(start) if c != '_']
        target_indices = [(i, c) for i, c in enumerate(target) if c != '_']
        
        for (start_idx, piece), (target_idx, _) in zip(start_indices, target_indices):
            if piece == 'L' and start_idx < target_idx:
                return False
            if piece == 'R' and start_idx > target_idx:
                return False
        
        return True

# https://leetcode.com/problems/move-pieces-to-obtain-a-string
