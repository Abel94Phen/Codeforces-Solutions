t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    while n:
        n //= 2
        count += 1
    print((1 << (count - 1)) - 1)