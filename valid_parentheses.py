class Solution(object):
    def isValid(self, s):
      
        # Stack to keep track of opening brackets
        stack = []
        # Hash map to store the mapping of closing to opening brackets
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack if it's not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the expected opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets are matched
        return not stack

# https://leetcode.com/problems/valid-parentheses
