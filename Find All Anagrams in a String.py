class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        dic_p = defaultdict(int)
        dic_s = defaultdict(int)
        for i in range(len(p)):
            dic_p[p[i]] += 1
            dic_s[s[i]] += 1
        res = [0] if dic_p==dic_s else[]
        l = 0
        for r in range(len(p),len(s)):
            dic_s[s[r]] += 1
            dic_s[s[l]] -= 1 
            if dic_s[s[l]] == 0:
                del dic_s[s[l]]
            l += 1
            if dic_s == dic_p:
                res.append(l)
        return res
