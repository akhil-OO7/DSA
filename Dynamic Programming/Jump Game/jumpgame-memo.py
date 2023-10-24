class Solution:
    # TLE  
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dfs(i):
            if i == n - 1:
                return True
            if i >= n:
                return False
            res = False
            for j in range(1, nums[i] + 1):
                res = res or dfs(i + j)
            return res
        return dfs(0)
