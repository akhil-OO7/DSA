class Solution:
    def search(self, pat, txt):
        m, n = len(txt), len(pat)
        lps = [0] * n
        prevLPS, i = 0, 1
        while i < n:
            if pat[i] == pat[prevLPS]:
                prevLPS += 1
                lps[i] = prevLPS
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]                
        res = []
        i, j = 0, 0
        while i < m:
            if txt[i] == pat[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            
            if j == n:
                res.append(i - j + 1)
                j = lps[j - 1]  
        return res
