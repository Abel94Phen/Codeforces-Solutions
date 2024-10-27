t = int(input())

for _ in range(t):
    n, l, r, k = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()
    bought = 0
    for price in array:
        if l <= price <= r and price <= k:
            bought += 1
            k -= price
    print(bought)