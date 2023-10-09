class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for j in range(n):
            i = 0
            while j+i < n and i < m and haystack[j+i] == needle[i]:
                if i == m-1:
                    return j
                i+=1
        return -1