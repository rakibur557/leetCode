class Solution(object):
    def maxCount(self, banned, n, maxSum):
      
        # Convert banned to a set for O(1) lookups
        banned_set = set(banned)
        
        # Initialize variables
        current_sum = 0
        count = 0
        
        # Iterate through the range [1, n]
        for i in range(1, n + 1):
            # Skip banned integers
            if i in banned_set:
                continue
            
            # Check if adding the current number exceeds maxSum
            if current_sum + i > maxSum:
                break
            
            # Add the number to the sum and increment count
            current_sum += i
            count += 1
        
        return count

# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i
