class Solution(object):
    def checkIfExist(self, arr):
       
        seen = set()  # To keep track of elements we have encountered
        
        for num in arr:
            # Check if current number satisfies the condition with any seen number
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)  # Add the current number to the set
            
        return False
    
# https://leetcode.com/problems/check-if-n-and-its-double-exist
