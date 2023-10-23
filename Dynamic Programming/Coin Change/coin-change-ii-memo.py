class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def dfs(i, cur):
            if (i, cur) in memo:
                return memo[(i, cur)]
            if cur == 0:
                return 1
            if i == n or cur < 0:
                return 0
            if cur < coins[i]:
                memo[(i, cur)] = dfs(i + 1, cur)
                return memo[(i, cur)]
            take = dfs(i, cur - coins[i])
            skip = dfs(i + 1, cur)
            memo[(i, cur)] = take + skip
            return memo[(i, cur)]

        return dfs(0, amount)
