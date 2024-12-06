class Solution(object):
    def mySqrt(self, x):
    
        if x == 0 or x == 1:
            return x  # Square root of 0 or 1 is the number itself
        
        low, high = 0, x
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid  # Exact square root found
            elif mid * mid < x:
                result = mid  # Store the potential answer
                low = mid + 1
            else:
                high = mid - 1
        
        return result
