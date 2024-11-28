class Solution(object):
    def isMatch(self, s, p):
        # Initialize a DP table with size (len(s)+1) x (len(p)+1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: Empty string matches with empty pattern
        dp[0][0] = True
        
        # Handle patterns with '*'
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  # '*' can match zero preceding elements
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' can match zero preceding elements or one/more preceding elements
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))
        
        # Return whether the entire string and pattern match
        return dp[len(s)][len(p)]

# https://leetcode.com/problems/regular-expression-matching