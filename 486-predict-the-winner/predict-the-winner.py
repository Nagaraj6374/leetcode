class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        # dp[i] will store the max relative score difference for subarray nums[i...j]
        dp = list(nums)

        # Build DP table from shorter subarrays to longer ones
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i] = max(nums[i] - dp[i + 1], nums[j] - dp[i])

        # Player 1 wins if max relative score >= 0
        return dp[0] >= 0