from collections import defaultdict
n = int(input())
k = int(input())
graph = []
dic=defaultdict(list)
for _ in range(k):
    row = list(map(int,input().split()))
    graph.append(row)
for i in range(len(graph)):
    if graph[i][0] == 1:
        dic[str(graph[i][1])].append(str(graph[i][2]))
        dic[str(graph[i][2])].append(str(graph[i][1]))
    elif graph[i][0] == 2:
        print(' '.join(dic[str(graph[i][1])]))
