class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r,n = 0,0,len(fruits)
        max_=0
        dic = defaultdict(int)
        if len(fruits) == 1:return 1
        while r<n:
            dic[fruits[r]] += 1
            if len(dic) <= 2:
                max_=max(max_,r-l+1)
            if len(dic) > 2:
                if dic[fruits[l]] == 1:
                    del dic[fruits[l]]
                else:
                    dic[fruits[l]] -= 1
                l += 1
            r += 1
        return max_ 
