t = int(input())
for _ in range(t):
    l, r = map(int, input().split())

    odds = sum(i%2 for i in range(l, r + 1))
    print(odds//2)