class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
       
        # Step 1: Compute the sum of every subarray of length k
        n = len(nums)
        k_sum = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        k_sum[0] = current_sum

        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            k_sum[i] = current_sum

        # Step 2: Compute the max left indices and max right indices
        left_max = [0] * len(k_sum)
        right_max = [0] * len(k_sum)

        max_index = 0
        for i in range(len(k_sum)):
            if k_sum[i] > k_sum[max_index]:
                max_index = i
            left_max[i] = max_index

        max_index = len(k_sum) - 1
        for i in range(len(k_sum) - 1, -1, -1):
            if k_sum[i] >= k_sum[max_index]:  # Use >= to ensure lexicographical order
                max_index = i
            right_max[i] = max_index

        # Step 3: Find the maximum sum by considering middle subarray
        max_total = 0
        result = [-1, -1, -1]

        for middle in range(k, len(k_sum) - k):
            left = left_max[middle - k]
            right = right_max[middle + k]

            total = k_sum[left] + k_sum[middle] + k_sum[right]
            if total > max_total:
                max_total = total
                result = [left, middle, right]

        return result
