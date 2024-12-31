class Solution(object):
    def mincostTickets(self, days, costs):
        # Use a set for O(1) lookups to check if a day requires travel
        travel_days = set(days)
        
        # The maximum day we need to consider
        last_day = days[-1]

        # Create a dp array where dp[i] represents the minimum cost to cover up to day i
        dp = [0] * (last_day + 1)

        for i in range(1, last_day + 1):
            if i not in travel_days:
                # If it's not a travel day, the cost remains the same as the previous day
                dp[i] = dp[i - 1]
            else:
                # Calculate the cost considering all ticket types
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],  # 1-day pass
                    dp[max(0, i - 7)] + costs[1],  # 7-day pass
                    dp[max(0, i - 30)] + costs[2]  # 30-day pass
                )

        return dp[last_day]
