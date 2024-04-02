t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split()))
    operations = 0
    
    while a <= c and b <= c:
        if a <= b:
            a += b
        else:
            b += a
        operations += 1

    print(operations)