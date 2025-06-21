n = int(input())
cost = list(map(int, input().split()))
drop = list(map(int, input().split()))
cost.reverse()
cost.extend(drop)
total = sum(cost[:n-1])
result = float("inf")
left = 0
for right in range(n - 1, 2*n):
    total += cost[right]
    result = min(result, total)
    total -= cost[left]
    left += 1
print(result)
