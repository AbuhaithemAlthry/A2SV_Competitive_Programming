n = int(input())
graph = []


for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

res = 0

for row in graph:
    for j in row:
        if j == 1:
            res += 1

print(res//2)
