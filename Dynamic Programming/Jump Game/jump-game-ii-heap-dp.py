class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[0] = 0
        minH = [(0, 0)]        # (jump, idx)
        for i in range(n):
            while minH and minH[0][1] + nums[minH[0][1]] < i:
                heapq.heappop(minH)
            dp[i] = min(dp[i], 1 + minH[0][0])
            heapq.heappush(minH, (dp[i], i))
        
        return dp[-1]
