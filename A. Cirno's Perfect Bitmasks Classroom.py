t = int(input())

for _ in range(t):
    x = int(input())
    y = 0
    for i in range(x.bit_length()):
        if x & (1 << i):
            y = 1 << i
            break
            
    if y == x:
        if y & 1:
            y += 2
        else:
            y += 1
    print(y)
