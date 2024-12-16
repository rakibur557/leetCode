class Solution(object):
    def divide(self, dividend, divisor):
        # Define the 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle edge cases for overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # Overflow case

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Convert dividend and divisor to positive values
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize the quotient
        quotient = 0

        # Perform the division using bitwise operations
        while dividend >= divisor:
            temp_divisor, num_shifts = divisor, 0
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_shifts += 1

            # Subtract the largest shifted divisor from the dividend
            dividend -= temp_divisor

            # Add the corresponding power of two to the quotient
            quotient += 1 << num_shifts

        # Apply the sign to the result
        if negative:
            quotient = -quotient

        # Clamp the result within the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))
