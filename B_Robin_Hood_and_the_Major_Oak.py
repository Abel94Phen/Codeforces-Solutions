t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    total = (2 * n - k + 1) * k // 2
    if total % 2:
        print("NO")
    else:
        print("YES")