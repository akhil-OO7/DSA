class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        memo = {}
        def solve(i, N):
            if (i, N) in memo:
                return memo[(i, N)]
            if i > N:
                return 0
            rob = nums[i] + solve(i + 2, N)
            notRob = solve(i + 1, N)
            memo[(i, N)] = max(rob, notRob)
            return memo[(i, N)]

        return max(solve(0, n - 2), solve(1, n - 1))
