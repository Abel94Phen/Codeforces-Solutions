k, r = list(map(int, input().split()))
price = k
while k % 10:
    if not (k - r) % 10:
        break
    k += price
print(k//price)