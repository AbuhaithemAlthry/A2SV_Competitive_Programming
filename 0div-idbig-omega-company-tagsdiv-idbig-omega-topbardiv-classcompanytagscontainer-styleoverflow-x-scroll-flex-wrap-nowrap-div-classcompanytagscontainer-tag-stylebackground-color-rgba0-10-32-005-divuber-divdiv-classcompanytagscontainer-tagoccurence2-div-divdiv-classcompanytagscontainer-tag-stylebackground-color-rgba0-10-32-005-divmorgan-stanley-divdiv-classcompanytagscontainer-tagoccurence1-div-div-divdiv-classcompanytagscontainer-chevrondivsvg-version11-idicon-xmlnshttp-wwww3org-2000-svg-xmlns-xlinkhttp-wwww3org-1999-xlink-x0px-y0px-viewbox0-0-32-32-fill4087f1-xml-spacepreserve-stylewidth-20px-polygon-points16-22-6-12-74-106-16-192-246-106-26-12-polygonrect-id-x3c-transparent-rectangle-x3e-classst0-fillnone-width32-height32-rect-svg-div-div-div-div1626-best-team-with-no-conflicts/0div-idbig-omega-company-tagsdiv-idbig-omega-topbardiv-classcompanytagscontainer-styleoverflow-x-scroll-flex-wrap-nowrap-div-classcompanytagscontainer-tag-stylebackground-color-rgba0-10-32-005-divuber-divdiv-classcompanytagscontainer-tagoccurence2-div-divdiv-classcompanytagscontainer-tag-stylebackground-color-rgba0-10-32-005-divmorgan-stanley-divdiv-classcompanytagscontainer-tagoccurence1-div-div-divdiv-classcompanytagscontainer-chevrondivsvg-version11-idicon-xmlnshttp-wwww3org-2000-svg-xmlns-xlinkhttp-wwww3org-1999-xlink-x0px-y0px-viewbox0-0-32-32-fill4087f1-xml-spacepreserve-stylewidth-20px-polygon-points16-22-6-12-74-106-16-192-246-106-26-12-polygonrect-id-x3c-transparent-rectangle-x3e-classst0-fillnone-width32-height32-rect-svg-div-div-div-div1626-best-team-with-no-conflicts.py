class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        new_list = list(zip(ages, scores))
        new_list = sorted(new_list)
        memo = [[None for i in range(len(scores)+1)] for j in range(len(scores)+1)]
        def solve(i, prev_i):
            if i == len(scores):
                return 0
            if memo[i][prev_i]:
                return memo[i][prev_i]
            take = 0
            dontTake = 0 + solve(i + 1, prev_i)
            if prev_i == -1 or new_list[i][1] >= new_list[prev_i][1]:
                take = new_list[i][1] + solve(i + 1, i)
            memo[i][prev_i] = max(take, dontTake)
            return memo[i][prev_i]
        
        n = len(scores)
        return solve(0, -1)