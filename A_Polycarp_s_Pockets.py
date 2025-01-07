n = int(input())
coins = list(map(int, input().split()))
counts = {}
for coin in coins:
    if coin not in counts:
        counts[coin] = 0
    counts[coin] += 1
print(max(counts.values()))