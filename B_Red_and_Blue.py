t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))            
    for i in range(1, n):
        a[i] += a[i - 1]          
    m = int(input())
    b = list(map(int, input().split()))
    for i in range(1, m):
        b[i] += b[i - 1]  
    print(max(0, max(a)) + max(0, max(b)))   