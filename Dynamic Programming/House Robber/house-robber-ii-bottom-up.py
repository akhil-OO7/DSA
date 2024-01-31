class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        return max(self.help(0, n - 1, nums), self.help(1, n, nums))
    
    def help(self, s, n, nums):
        rob1, rob2 = 0, 0

        for i in range(s, n):
            tmp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
            return rob2
