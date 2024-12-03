class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()  # Sort the array to enable two-pointer technique
        closest_sum = float('inf')  # Initialize closest_sum to infinity

        for i in range(len(nums) - 2):  # Iterate over the array
            left, right = i + 1, len(nums) - 1  # Two-pointer approach

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Check if the current sum is closer to the target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1  # Move the left pointer to increase the sum
                elif current_sum > target:
                    right -= 1  # Move the right pointer to decrease the sum
                else:
                    # If the exact target is found, return it
                    return current_sum

        return closest_sum
# https://leetcode.com/problems/3sum-closest
