items, queries = list(map(int, input().split()))

prices = list(map(int, input().split()))
prices.sort()

sums = [0 for _ in range(items + 1)]

for i in range(items):
    sums[i + 1] += sums[i] + prices[i]

print(sums)

for _ in range(queries):
    x, y = list(map(int, input().split()))
    print(sums[items - x + y] - sums[items - x])