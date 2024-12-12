class Solution(object):
    def climbStairs(self, n):

        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize variables for dp[n-2] and dp[n-1]
        prev2, prev1 = 1, 2

        # Compute dp[n] iteratively
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1
