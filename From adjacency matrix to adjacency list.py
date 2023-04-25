n = int(input())

graph_mat = []

for _ in range(n):
    row = list(map(int, input().split()))
    graph_mat.append(row)

from collections import defaultdict
graph = defaultdict(list)

for i in range(len(graph_mat)):
    for j in range(len(graph_mat[0])):
        if graph_mat[i][j] == 1:
            graph[i].append(j + 1)
    print(len(graph[i]),*graph[i])
