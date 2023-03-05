class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r,n = 0,0,len(s)
        dic = defaultdict(int)
        res=0
        max_fr = 0
        while r < n:
            r_char = s[r]
            dic[r_char] += 1
            max_fr = max(max_fr,dic[r_char])
            while (r-l+1)-max_fr > k:
                if dic[s[l]] == 1:
                    del dic[s[l]] 
                else:
                    dic[s[l]] -= 1
                l+=1
            res= max(res,r-l+1)
            r+=1
        return res
