t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_a, max_b = max(a), max(b)
    if max_a < max_b:
        a, b = b, a
        max_a, max_b = max_b, max_a

    for i in range(n):
        if b[i] > a[i]:
            b[i], a[i] = a[i], b[i]
    
    max_b = max(b)
    print(max_a * max_b)
