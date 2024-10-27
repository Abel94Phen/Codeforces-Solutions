t = int(input())

for _ in range(t):
    r, b, d = map(int, input().split())
    
    if (max(r, b) - min(r, b)) / min(r, b) <= d:
        print("YES")
    else:
        print("NO")