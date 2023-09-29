class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        sd = defaultdict(list)
        for i,c in enumerate(s):
            sd[c].append(i)
        
        ct = 0
        for w in words:            
            pre = -1
            for c in w:
                pos = bisect.bisect(sd[c], pre)
                if pos==len(sd[c]): break
                pre = sd[c][pos]
            else:ct+=1
        return ct
                