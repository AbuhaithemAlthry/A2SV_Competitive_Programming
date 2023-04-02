t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    mx = 0
    for i in range(n):
        for j in range(m):
            now = 0
            ci, cj = i, j
            while ci >= 0 and ci < n and cj >= 0 and cj < m:
                now += a[ci][cj]
                ci -= 1
                cj -= 1
            ci, cj = i, j
            while ci >= 0 and ci < n and cj >= 0 and cj < m:
                now += a[ci][cj]
                ci += 1
                cj -= 1
            ci, cj = i, j
            while ci >= 0 and ci < n and cj >= 0 and cj < m:
                now += a[ci][cj]
                ci -= 1
                cj += 1
            ci, cj = i, j
            while ci >= 0 and ci < n and cj >= 0 and cj < m:
                now += a[ci][cj]
                ci += 1
                cj += 1
            now -= a[i][j] * 3
            mx = max(mx, now)
    print(mx)
