n = int(input())
for _ in range(n):
    p, m = map(int,input().split())
    high = (p+m)//4
    print(min(min(m,p),high))
