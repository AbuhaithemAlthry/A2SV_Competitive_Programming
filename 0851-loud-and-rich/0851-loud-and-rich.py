class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        for en, st in richer:
            graph[st].append(en)
        n = len(quiet)
        ans = [0] * n
            
        def dfs(node):
            if ans[node] != 0:
                return ans[node]
            
            ans[node] = node
            for child in graph[node]:
                cand = dfs(child)
                if quiet[cand] < quiet[ans[node]]:
                    ans[node] = cand
            return ans[node]
        
        for i in range(n):
            dfs(i)
        return ans