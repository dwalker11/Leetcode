class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(nums):
                return 0

            return max(dp(i + 1), dp(i + 2) + nums[i])

        return dp(0)
