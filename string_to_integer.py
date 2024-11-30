class Solution(object):
    def myAtoi(self, s):
        # Step 1: Ignore leading whitespace
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Check for sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        # Step 3: Read digits and form the number
        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1

        # Step 4: Apply the sign
        num *= sign

        # Step 5: Clamp the result to the 32-bit signed integer range
        int_min, int_max = -2**31, 2**31 - 1
        if num < int_min:
            return int_min
        if num > int_max:
            return int_max

        return num

# Driver code to test the implementation
if __name__ == "__main__":
    param_1 = "42"  # Replace with your input
    solution = Solution()
    print(solution.myAtoi(param_1))  # Output: 42

# https://leetcode.com/problems/string-to-integer-atoi/