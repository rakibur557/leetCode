class Solution(object):
    def maxScore(self, s):
        """
        NEW YEAR FIRST CODE: 2025
        """
        max_score = 0

        # Iterate over all possible split points, excluding the last character
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]

            # Calculate the score for this split
            score = left.count('0') + right.count('1')

            # Update the maximum score
            max_score = max(max_score, score)

        return max_score

