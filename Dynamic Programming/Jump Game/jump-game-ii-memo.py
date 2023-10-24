from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if i == n - 1:
                return 0
            if i >= n:
                return inf
            res = inf
            for j in range(1, nums[i] + 1):
                res = min(res, 1 + dfs(i + j))
            return res
        return dfs(0)
