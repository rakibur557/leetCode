class Solution(object):
    def candy(self, ratings):
        
        n = len(ratings)
        
        # Step 1: Initialize candies array with 1 candy for each child
        candies = [1] * n
        
        # Step 2: Traverse from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Step 3: Traverse from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Step 4: Calculate the total candies
        return sum(candies)
