class Solution(object):
    def generateParenthesis(self, n):
        
        result = []

        def backtrack(current, open_count, close_count):
            # If the current combination is complete
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # Add an open parenthesis if possible
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()  # Backtrack

            # Add a close parenthesis if possible
            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()  # Backtrack

        # Start the backtracking with an empty string
        backtrack([], 0, 0)
        return result
