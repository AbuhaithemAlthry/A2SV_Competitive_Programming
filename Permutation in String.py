class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        dic_s1 = defaultdict(int)
        dic_s2 = defaultdict(int)
        for i in range(len(s1)):
            dic_s1[s1[i]] += 1
            dic_s2[s2[i]] += 1
        if dic_s1 == dic_s2 : return True
        l=0
        n = len(s1)
        r = n
        while r<len(s2):
            dic_s2[s2[r]] += 1
            dic_s2[s2[l]] -= 1 
            if dic_s2[s2[l]] == 0:
                del dic_s2[s2[l]]
            if dic_s1 == dic_s2:
                return True
            r += 1
            l += 1
        return False
            
