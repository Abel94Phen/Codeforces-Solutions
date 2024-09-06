t = int(input())

for _ in range(t):
    n, m, x = map(int, input().split())
    x -= 1
    r = x // n
    c = x % n
    print(c * m + r + 1)
