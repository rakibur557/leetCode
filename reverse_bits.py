class Solution:
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            # Extract the least significant bit of n
            bit = n & 1
            # Shift the result to the left to make space for the new bit
            result = (result << 1) | bit
            # Shift n to the right to process the next bit
            n >>= 1
        return result
