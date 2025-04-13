t = int(input())
for _ in range(t):
    l, r, d, u = list(map(int, input().split()))
    if l == r == d == u:
        print("Yes")
    else:
        print("No")