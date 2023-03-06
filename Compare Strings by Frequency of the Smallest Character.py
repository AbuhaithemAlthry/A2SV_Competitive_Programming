class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def helper(w: str)-> int:
            cnt = 0
            min_al=min(w)
            for i in w:
                if i == min_al:
                    cnt += 1
            return cnt
        n = len(words)
        res = []
        words_c = []
        for word in words:
            words_c.append(helper(word))
        words_c.sort()
        
        for query in queries:
            m = helper(query)
            l = -1
            r = len(words)
            while r > l+1:
                mid = l + (r - l)//2
                if words_c[mid] > m:
                    r = mid
                elif words_c[mid] <= m:
                    l = mid
            res.append(n-r)    
        return res
