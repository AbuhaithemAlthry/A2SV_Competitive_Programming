from collections import defaultdict
n = int(input())
graph = defaultdict(list)
source = []
sink = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        graph[i+1].append(row[j])
for i in range(n):
    t = 1
    if t not in graph[i+1]:
        source.append(str(i+1))
        bool_= True
        for j in range(n):
            if graph[j+1][i] == t:
                bool_ = False
        if bool_:
            sink.append(str(i+1))
    else:
        bool_= True
        for j in range(n):
            if graph[j+1][i] == t:
                bool_ = False
        if bool_:
            sink.append(str(i+1))

print(len(sink),' '.join(sink))
print(len(source),' '.join(source))
