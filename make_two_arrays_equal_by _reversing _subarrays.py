class Solution(object):
    def canBeEqual(self, target, arr):
        # Sort both arrays and compare them
        return sorted(target) == sorted(arr)
