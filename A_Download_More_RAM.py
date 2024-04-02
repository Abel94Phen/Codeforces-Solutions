t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    
    mapping = []
    
    for i in range(n):
        mapping.append((a[i], b[i]))
    
    mapping.sort(key = lambda x:x[0])
    
    
    i = 0
    while i < n and mapping[i][0] <= k:
        k += mapping[i][1]
        i += 1
    
    print(k)