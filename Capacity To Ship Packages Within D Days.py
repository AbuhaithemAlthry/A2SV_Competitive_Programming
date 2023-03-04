class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights) -1
        high = sum(weights)
        
        def check(n:int) -> bool:
            cap = n
            n_ship = 1
            for weight in weights:
                if cap - weight < 0:
                    n_ship += 1
                    cap = n
                cap -= weight
            return n_ship <= days
            
        while high > low + 1:
            mid = low + (high - low)//2
            if check(mid):
                high = mid
            else:
                low = mid
        return high
