items, queries = list(map(int, input().split()))

prices = list(map(int, input().split()))
count_array = [0 for _ in range(max(prices))]
for price in prices:
    count_array[price - 1] += 1

prices = []

for i in range(items):
    while count_array[i] > 0:
        prices.append(i + 1)
        count_array[i] -= 1


for _ in range(queries):
    x, y = list(map(int, input().split()))
    received_free = 0
    for i in range(items - x, items - x + y):
        received_free += prices[i]
    print(received_free)