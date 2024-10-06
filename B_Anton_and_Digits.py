k2, k3, k5, k6 = map(int, input().split())

result = 0

if k2 >= max(k5, k6):
    limiter = min(k5, k6)
    k2 -= limiter
    result += 256 * min(k5, k6)
    k5, k6 = k5 - limiter, k6 - limiter
    result += 32 * min(k2, k3)
    k2, k3 = k2 - min(k2, k3), k3 - min(k2, k3)
else:
    limiter = min(k2, k5, k6)
    result += 256 * limiter
    k2, k5, k6 = k2 - limiter, k5 - limiter, k6 - limiter
    result += 32 * min(k2, k3)
    k2, k3 = k2 - min(k2, k3), k3 - min(k2, k3)
print(result)