class Solution(object):
    def minimumSize(self, nums, maxOperations):
        
        def canAchievePenalty(p):
            # Check if it's possible to achieve penalty `p` with maxOperations
            operations = 0
            for balls in nums:
                if balls > p:
                    operations += (balls - 1) // p
                if operations > maxOperations:
                    return False
            return True

        # Binary search for the minimum penalty
        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            if canAchievePenalty(mid):
                high = mid  # Try for a smaller penalty
            else:
                low = mid + 1  # Increase penalty
        return low
