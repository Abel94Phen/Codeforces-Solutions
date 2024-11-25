t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    total = sum(prices)
    if total%n:
        total += n - total%n
    print(total // n)