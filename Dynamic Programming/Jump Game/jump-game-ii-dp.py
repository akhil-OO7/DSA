class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], 1 + dp[j])
        
        return dp[-1]
