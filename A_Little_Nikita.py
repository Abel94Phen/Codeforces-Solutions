t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if n < m:
        print("No")
    else:
        if (n - m) % 2:
            print("No")
        else:
            print("Yes")