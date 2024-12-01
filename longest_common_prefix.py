class Solution(object):
    def longestCommonPrefix(self, strs):
       
        if not strs:
            return ""  # Edge case: empty list
        
        # Step 1: Sort the array
        strs.sort()
        
        # Step 2: Compare the first and last strings
        first, last = strs[0], strs[-1]
        i = 0
        
        # Step 3: Find the common prefix
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]  # Return the common prefix

# https://leetcode.com/problems/longest-common-prefix