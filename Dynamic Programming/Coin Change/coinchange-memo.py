class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def dfs(i, cur):
            if cur == 0:
                return 0
            if cur < 0:
                return inf
            if i == n:
                return inf
            take = 1 + dfs(i, cur - coins[i])
            skip = dfs(i + 1, cur)
            return min(take, skip)
        res = dfs(0, amount)
        return res if res != inf else -1
