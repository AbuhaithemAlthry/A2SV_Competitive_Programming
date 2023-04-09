t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ok = True
    for i in range(1, n):
        ok &= (a[i] - a[i - 1] <= 1)
    if ok:
        print("YES")
    else:
        print("NO")
