class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            n = n & (n - 1)  # Clear the least significant set bit
            count += 1
        return count
