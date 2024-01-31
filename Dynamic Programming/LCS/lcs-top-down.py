class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = {}
        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m or j == n:
                return 0

            if i not in range(m) or j not in range(n):
                return inf

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + solve(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = max(solve(i, j + 1), solve(i + 1, j))
            return memo[(i, j)]

        return solve(0, 0)
    
