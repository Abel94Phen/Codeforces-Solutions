t = int(input())
for _ in range(t):
    n = int(input())
    cats = [i for i in range(1, n + 1)]
    for i in range(0, n - 1, 2):
        cats[i], cats[i + 1] = cats[i + 1], cats[i]
    
    if n%2:
        cats[-1], cats[-3] = cats[-3], cats[-1]
    
    print(*cats)