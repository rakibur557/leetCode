class Solution(object):
    def plusOne(self, digits):
        # Start from the last digit and handle carry
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, increment it and return the result
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise, set the current digit to 0 and continue to the next digit
            digits[i] = 0
        
        # If we have exited the loop, it means we had a carry that added a new digit at the beginning
        return [1] + digits

# https://leetcode.com/problems/plus-one/