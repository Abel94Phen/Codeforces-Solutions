n, k = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
excess = 0
status = True
for i in range(1, n):
    if (prices[i] - prices[0])%k == 0:
        excess += prices[i] - prices[0]
    else:
        status = False
        break
if not status:
    print(-1)
else:
    print(excess // k)
