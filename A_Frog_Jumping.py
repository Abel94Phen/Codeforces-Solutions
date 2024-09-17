t = int(input())

for _ in range(t):
    a, b, k = map(int, input().split())
    if k%2:
        print((k - k//2)*a - (k//2)*b)
    else:
        print((k//2)*a - (k//2)*b)