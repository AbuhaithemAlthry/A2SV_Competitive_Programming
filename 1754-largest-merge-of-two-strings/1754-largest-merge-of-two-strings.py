class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1 , w2  , ans = 0 ,0 , ""
        while w1 < len(word1)  and w2 < len(word2):
            if word1[w1:] > word2[w2:]:
                ans+=word1[w1]
                w1+=1
            else:
                ans+=word2[w2]
                w2+=1
        ans+=word1[w1:] + word2[w2:]
        return ans
