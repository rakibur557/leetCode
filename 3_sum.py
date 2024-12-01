class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Step 1: Sort the array
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers to find pairs
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for nums[left] and nums[right]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move the pointers
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # Increase the sum
                else:
                    right -= 1  # Decrease the sum
        
        return result

# https://leetcode.com/problems/3sum