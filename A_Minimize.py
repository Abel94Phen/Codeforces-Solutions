t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    result = float('inf')
    for c in range(a, b + 1):
        result = min(result, (c - a) + (b - c))
    print(result)