items, queries = list(map(int, input().split()))

prices = list(map(int, input().split()))
prices.sort()

sums = [0 for _ in range(items + 1)]

for i in range(items):
    sums[i + 1] += sums[i] + prices[i]

for _ in range(queries):
    x, y = list(map(int, input().split()))
    last_x = sums[-1] - sums[items - x]
    last_x_y = sums[-1] - sums[items - (x - y)]
    print(last_x - last_x_y)