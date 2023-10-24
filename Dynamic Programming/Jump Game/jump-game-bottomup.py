class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n    # dp[i] represents if we can reach the ith index
        dp[0] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if j + nums[j] >= i and dp[j] == True:
                    dp[i] = True
                    break
        
        return dp[-1]
