class Solution(object):
    def firstMissingPositive(self, nums):
       
        n = len(nums)

        # Step 1: Place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Step 2: Find the first index where the number is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: If all numbers are in place, return n + 1
        return n + 1
