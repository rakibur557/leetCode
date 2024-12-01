class Solution(object):
    def smallestNumber(self, num, t):

        def is_zero_free(number):
            # Check if the number contains any '0'
            return '0' not in number

        def product_of_digits(number):
            # Calculate the product of the digits of the number
            product = 1
            for digit in number:
                product *= int(digit)
                # If the product exceeds t and isn't divisible, no need to continue
                if product > t and product % t != 0:
                    return -1
            return product

        # Start from the given number
        current = int(num)

        # Iterate until a valid number is found
        while True:
            current_str = str(current)
            if is_zero_free(current_str):
                product = product_of_digits(current_str)
                if product != -1 and product % t == 0:
                    return current_str
            # Increment the number
            current += 1
            # Break if no solution exists (this is for large t constraints)
            if current > 10 ** len(num) + 1e6:  # Optimized upper limit
                return "-1"


# https://leetcode.com/problems/smallest-divisible-digit-product-ii