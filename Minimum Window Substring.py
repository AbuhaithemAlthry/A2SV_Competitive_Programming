class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        count_w = defaultdict(int)
        curr_w = defaultdict(int)
        
        for i in t:
            count_w[i]+=1
        
        l = 0
        need = len(count_w)
        have = 0
        res_win = [-1,-1]
        res = float('inf')
        
        for r in range(len(s)):
            curr_w[s[r]]+=1

            if s[r] in count_w and curr_w[s[r]] == count_w[s[r]]:
                have+=1

            while have == need:
                if (r-l+1) < res:
                    res = r-l+1
                    res_win = [l , r]

                curr_w[s[l]] -= 1

                if s[l] in count_w and curr_w[s[l]] < count_w[s[l]]:
                    have-=1
                l += 1 
        l,r = res_win
        return "".join(s[l:r+1]) if res != float('-inf') else ""
