class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costDiff = [(cost[0] - cost[1], i) for i, cost in enumerate(costs)]

        costDiff.sort()
        n = len(costs) // 2
        
        totalCost = 0
        
        for i, (_, idx) in enumerate(costDiff):
            if i < n:
                totalCost += costs[idx][0]
            else:
                totalCost += costs[idx][1]
                
        return totalCost
