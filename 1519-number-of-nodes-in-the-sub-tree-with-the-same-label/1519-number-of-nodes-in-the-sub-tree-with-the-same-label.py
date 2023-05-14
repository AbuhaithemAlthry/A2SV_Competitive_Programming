class Solution:
    def dfs(self, node: int, parent: int, adj: List[List[int]], labels: str, ans: List[int]) -> List[int]:
        node_counts = [0] * 26
        node_counts[ord(labels[node]) - ord('a')] = 1

        for child in adj[node]:
            if child == parent:
                continue
            child_counts = self.dfs(child, node, adj, labels, ans)
            for i in range(26):
                node_counts[i] += child_counts[i]

        ans[node] = node_counts[ord(labels[node]) - ord('a')]
        return node_counts

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        ans = [0] * n
        self.dfs(0, -1, adj, labels, ans)

        return ans