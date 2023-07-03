class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        n=len(s)
        seen = defaultdict(int)
        max_ = 0
        while r < n:
            if s[r] not in seen:
                seen[s[r]]+=1
                max_ = max(max_,len(seen))
                r+=1
            else:
                del seen[s[l]]
                l+=1
        print(max_)
        return max_
            