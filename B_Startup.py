t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    brands = [0 for _ in range(k)]
    for _ in range(k):
        b, c = map(int, input().split())
        brands[b - 1] += c
    brands.sort(reverse=True)
    result = 0
    for i in range(min(n, k)):
        result += brands[i]
    print(result)