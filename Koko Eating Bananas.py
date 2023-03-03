class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        high = max(piles) + 1
        def possible(n: int) -> bool:
            sum_hour = 0
            for i in piles:
                sum_hour += ceil(i/n)
            return True if sum_hour <= h else False

        while high > low + 1:
            mid = low + (high - low)//2
            if possible(mid):
                high = mid
            else:
                low = mid
        return high
