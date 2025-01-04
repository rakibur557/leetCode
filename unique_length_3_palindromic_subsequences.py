class Solution(object):
    def countPalindromicSubsequence(self, s):
    
        unique_palindromes = set()
        
        # Iterate over each possible middle character
        for i in range(1, len(s) - 1):
            left_chars = set(s[:i])  # Characters before the middle character
            right_chars = set(s[i + 1:])  # Characters after the middle character
            
            for char in left_chars:
                if char in right_chars:
                    unique_palindromes.add(char + s[i] + char)  # Create and add the palindrome
            
        return len(unique_palindromes)

