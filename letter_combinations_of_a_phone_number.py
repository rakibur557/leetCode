class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []  # No digits, return empty list

        # Digit to letter mapping
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        # Helper function for backtracking
        def backtrack(index, path):
            if index == len(digits):  # If the path is complete
                result.append("".join(path))  # Add to result
                return
            
            # Get letters for the current digit
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)  # Choose a letter
                backtrack(index + 1, path)  # Explore further
                path.pop()  # Backtrack (undo choice)

        # Start backtracking from the first digit
        backtrack(0, [])
        return result

# https://leetcode.com/problems/letter-combinations-of-a-phone-number