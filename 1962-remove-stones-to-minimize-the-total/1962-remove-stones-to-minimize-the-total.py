class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        x = [-i for i in piles]
        heapify(x)
        print(x)
        while k > 0:
            num = heappop(x)
            num//=2
            heappush(x,num)
            k-=1
        return -1*sum(x)