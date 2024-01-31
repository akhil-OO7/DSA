class Solution:
    def rob(self, nums: List[int]) -> int:
        n =  len(nums)
        @cache
        def solve(i):
            if i >= n:
                return 0
            take = nums[i] + solve(i + 2)
            skip = solve(i + 1)
            return max(take, skip)
        
        return solve(0)
            
