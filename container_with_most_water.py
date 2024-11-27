class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the width and area
            width = right - left
            if height[left] < height[right]:
                max_area = max(max_area, height[left] * width)
                left += 1  # Move the left pointer
            else:
                max_area = max(max_area, height[right] * width)
                right -= 1  # Move the right pointer

        return max_area
# https://leetcode.com/problems/container-with-most-water/
