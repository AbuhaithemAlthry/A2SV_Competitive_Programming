class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,n = 0,0,len(s)
        dic = defaultdict(int)
        max_ = 0
        while r<n:
            r_char = s[r]
            while r_char in dic:
                del dic[s[l]]
                l += 1
            dic[r_char] += 1
            max_=max(max_,r-l+1)
            r += 1
        return max_
